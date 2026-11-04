"""Render nested YAML flyer blocks to a single-page PDF."""
import copy
import pathlib

import qrcode
import reportlab.lib.colors
import reportlab.lib.pagesizes
import reportlab.lib.styles
import reportlab.lib.units
import reportlab.lib.utils
import reportlab.pdfbase.pdfmetrics
import reportlab.pdfbase.ttfonts
import reportlab.platypus
import reportlab.graphics.renderPDF
import svglib.svglib
import yaml


class FlyerError(ValueError):
	"""An authored flyer cannot be rendered."""


class QrCode(reportlab.platypus.Flowable):
	"""A linked, vector QR code with a four-module quiet zone."""

	def __init__(self, url: str, size: float, color: str, icon: pathlib.Path | None = None,
		label: str | None = None):
		super().__init__()
		self.url = url
		self.size = size
		self.color = color
		self.icon = icon
		self.label = label
		self.width = size
		self.height = size + (12 if label else 0)

	def draw(self) -> None:
		qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=4)
		qr.mask_pattern = 0
		qr.add_data(self.url)
		qr.make(fit=True)
		matrix = qr.get_matrix()
		step = self.size / len(matrix)
		qr_y = 12 if self.label else 0
		self.canv.setFillColor(reportlab.lib.colors.HexColor(self.color))
		for row, values in enumerate(matrix):
			for col, value in enumerate(values):
				if value:
					self.canv.rect(col * step, qr_y + self.size - (row + 1) * step, step, step, 0, 1)
		if self.icon:
			icon = svglib.svglib.svg2rlg(str(self.icon))
			icon_size = self.size * .23
			self.canv.setFillColor(reportlab.lib.colors.white)
			self.canv.roundRect((self.size - icon_size) / 2 - 2, qr_y + (self.size - icon_size) / 2 - 2,
				icon_size + 4, icon_size + 4, 3, 0, 1)
			icon.scale(icon_size / icon.width, icon_size / icon.height)
			reportlab.graphics.renderPDF.draw(icon, self.canv, (self.size - icon_size) / 2,
				qr_y + (self.size - icon_size) / 2)
		if self.label:
			self.canv.setFillColor(reportlab.lib.colors.HexColor(self.color))
			self.canv.setFont('Atkinson-Bold', 8)
			self.canv.drawCentredString(self.size / 2, 1, self.label)
		self.canv.linkURL(self.url, (0, qr_y, self.size, qr_y + self.size), relative=1, thickness=0)


class SvgImage(reportlab.platypus.Flowable):
	"""An SVG drawn as a ReportLab vector drawing."""

	def __init__(self, path: pathlib.Path, height: float):
		super().__init__()
		self.path = path
		self.height = height
		self.drawing = svglib.svglib.svg2rlg(str(path))
		if self.drawing is None:
			raise FlyerError(f'cannot read SVG: {path}')
		self.width = self.drawing.width * height / self.drawing.height

	def draw(self) -> None:
		self.drawing.scale(self.width / self.drawing.width, self.height / self.drawing.height)
		reportlab.graphics.renderPDF.draw(self.drawing, self.canv, 0, 0)


def _font_files() -> pathlib.Path:
	return pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'fonts'


def _register_fonts() -> None:
	font_dir = _font_files()
	reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont(
		'Atkinson', str(font_dir / 'AtkinsonHyperlegibleNext-Regular.ttf')))
	reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont(
		'Atkinson-Bold', str(font_dir / 'AtkinsonHyperlegibleNext-Bold.ttf')))


def _style(name: str, config: dict, styles: dict) -> reportlab.lib.styles.ParagraphStyle:
	base = copy.copy(styles['body']) if 'body' in styles else reportlab.lib.styles.ParagraphStyle('body')
	base.name = name
	base.fontName = 'Atkinson-Bold' if config.get('bold') else 'Atkinson'
	base.fontSize = config.get('size', 12)
	base.leading = config.get('leading', base.fontSize * 1.2)
	base.textColor = reportlab.lib.colors.HexColor(config.get('color', '#142535'))
	base.alignment = {'left': 0, 'center': 1, 'right': 2}.get(config.get('align', 'left'))
	base.spaceAfter = 0
	base.spaceBefore = 0
	return base


def _image(path: pathlib.Path, height: float) -> reportlab.platypus.Flowable:
	if not path.exists():
		raise FlyerError(f'missing asset: {path}')
	if path.suffix.lower() == '.svg':
		return SvgImage(path, height)
	reader = reportlab.lib.utils.ImageReader(str(path))
	width, natural_height = reader.getSize()
	return reportlab.platypus.Image(str(path), width * height / natural_height, height, mask='auto')


def _block(value: dict, root: pathlib.Path, styles: dict, width: float) -> reportlab.platypus.Flowable:
	if not isinstance(value, dict) or len(value) != 1:
		raise FlyerError('each layout item needs exactly one block type')
	kind, data = next(iter(value.items()))
	if kind == 'text':
		if isinstance(data, str):
			data = {'value': data}
		style_name = data.get('style', 'body')
		if style_name not in styles:
			raise FlyerError(f'unknown style: {style_name}')
		style = copy.copy(styles[style_name])
		if any(key in data for key in ('size', 'leading', 'color', 'align', 'bold')):
			style.fontName = 'Atkinson-Bold' if data.get('bold', style.fontName == 'Atkinson-Bold') else 'Atkinson'
			style.fontSize = data.get('size', style.fontSize)
			style.leading = data.get('leading', style.leading)
			style.textColor = reportlab.lib.colors.HexColor(data.get('color', style.textColor.hexval()))
			style.alignment = {'left': 0, 'center': 1, 'right': 2}.get(data.get('align', 'left'), style.alignment)
		text = data['value'].replace('\n', '<br/>')
		if data.get('url'):
			text = f'<link href="{data["url"]}">{text}</link>'
		return reportlab.platypus.Paragraph(text, style)
	if kind == 'image':
		data = {'path': data} if isinstance(data, str) else data
		return _image(root / data['path'], data['height'])
	if kind == 'qr':
		data = {'url': data} if isinstance(data, str) else data
		icon = root / data['icon'] if data.get('icon') else None
		return QrCode(data['url'], data.get('size', 76), data.get('color', '#000000'), icon,
			data.get('label'))
	if kind == 'rule':
		data = {} if data is None else data
		return reportlab.platypus.HRFlowable(width='100%', thickness=data.get('thickness', 1),
			color=reportlab.lib.colors.HexColor(data.get('color', '#00775F')), spaceBefore=0, spaceAfter=0)
	if kind in ('row', 'col'):
		data = data or {}
		gap = data.get('gap', 12)
		items = data.get('items', [])
		if not items:
			raise FlyerError(f'{kind} must contain items')
		if kind == 'col':
			children = [_block(item, root, styles, width) for item in items]
			return reportlab.platypus.Table([[child] for child in children], colWidths=[width],
				style=[('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
					('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), gap),
					('BOTTOMPADDING', (0, -1), (-1, -1), 0)])
		weights = [item.get('weight', 1) if isinstance(item, dict) else 1 for item in items]
		available = width - gap * (len(items) - 1)
		widths = [available * weight / sum(weights) for weight in weights]
		children = []
		for item, child_width in zip(items, widths):
			child = item.get('block', item) if isinstance(item, dict) else item
			children.append(_block(child, root, styles, child_width))
		return reportlab.platypus.Table([children], colWidths=widths,
			style=[('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), gap),
				('RIGHTPADDING', (-1, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
				('BOTTOMPADDING', (0, 0), (-1, -1), 0), ('VALIGN', (0, 0), (-1, -1), data.get('valign', 'TOP'))])
	raise FlyerError(f'unknown block type: {kind}')


def build(input_path: pathlib.Path, output_path: pathlib.Path) -> None:
	"""Build one flyer, without replacing output when validation fails."""
	with input_path.open() as handle:
		config = yaml.safe_load(handle)
	if not isinstance(config, dict) or 'layout' not in config:
		raise FlyerError('flyer needs a layout')
	_register_fonts()
	style_config = config.get('styles', {})
	styles = {'body': _style('body', style_config.get('body', {}), {})}
	for name, value in style_config.items():
		styles[name] = _style(name, value, styles)
	margin = config.get('page', {}).get('margin', 32)
	page_width, page_height = reportlab.lib.pagesizes.letter
	flowable = _block(config['layout'], input_path.parent, styles, page_width - margin * 2)
	output_path.parent.mkdir(parents=True, exist_ok=True)
	temporary_path = output_path.with_suffix('.tmp.pdf')
	document = reportlab.platypus.SimpleDocTemplate(str(temporary_path), pagesize=reportlab.lib.pagesizes.letter,
		leftMargin=margin, rightMargin=margin, topMargin=margin, bottomMargin=margin)
	try:
		document.build([flowable])
	except reportlab.platypus.LayoutError as error:
		temporary_path.unlink(missing_ok=True)
		raise FlyerError(f'content exceeds one Letter page: {error}') from error
	temporary_path.replace(output_path)
