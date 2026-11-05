import pathlib

import PIL.Image
import pypdf
import pytest

import flyerlib.render


def test_stvc_build_is_one_page_with_links(tmp_path: pathlib.Path) -> None:
	"""The production flyer remains one printable page with its destinations."""
	output_path = tmp_path / 'stvc.pdf'
	flyerlib.render.build(pathlib.Path('flyers/stvc/stvc.yaml'), output_path)
	reader = pypdf.PdfReader(str(output_path))
	assert len(reader.pages) == 1
	text = reader.pages[0].extract_text()
	assert 'Stump the' in text
	annotations = reader.pages[0]['/Annots']
	urls = {item.get_object()['/A']['/URI'] for item in annotations if '/A' in item.get_object()}
	assert 'https://www.youtube.com/@VossLab/streams' in urls
	assert 'https://vosslab.github.io/steroid-quest-into-the-nucleus/' in urls


def _image_objects(page: pypdf.PageObject) -> list:
	"""Return raster image XObjects from one rendered PDF page."""
	xobjects = page['/Resources'].get('/XObject', {})
	images = []
	for reference in xobjects.values():
		object_value = reference.get_object()
		if object_value.get('/Subtype') == '/Image':
			images.append(object_value)
	return images


def _source_pixels(path: pathlib.Path) -> tuple[int, int]:
	"""Read original raster dimensions without altering the source image."""
	with PIL.Image.open(path) as image:
		pixels = (image.width, image.height)
	return pixels


def test_shipped_rasters_keep_pixels_without_jpeg_pdf_encoding(tmp_path: pathlib.Path) -> None:
	"""Raster artwork keeps source pixels and never enters the PDF as JPEG data."""
	sources = {
		'stvc': [
			pathlib.Path('flyers/stvc/assets/dr-voss.png'),
			pathlib.Path('flyers/stvc/assets/episode-hosts.png'),
		],
		'github': [
			pathlib.Path('flyers/github/assets/profile.png'),
			pathlib.Path('flyers/github/assets/contribution_graph.webp'),
		],
	}
	for flyer_name, asset_paths in sources.items():
		output_path = tmp_path / f'{flyer_name}.pdf'
		flyerlib.render.build(pathlib.Path(f'flyers/{flyer_name}/{flyer_name}.yaml'), output_path)
		reader = pypdf.PdfReader(str(output_path))
		image_objects = _image_objects(reader.pages[0])
		embedded_pixels = {(image['/Width'], image['/Height']) for image in image_objects}
		for asset_path in asset_paths:
			assert _source_pixels(asset_path) in embedded_pixels
		for image in image_objects:
			filter_value = image.get('/Filter')
			assert '/DCTDecode' not in str(filter_value)


def test_printer_safe_margin_is_fixed_and_reaches_both_page_edges(tmp_path: pathlib.Path) -> None:
	"""The safe margin is a rendered-PDF contract, not only a YAML convention."""
	unsafe_source = tmp_path / 'unsafe.yaml'
	unsafe_source.write_text('page: {margin: 32}\nlayout: {col: {items: [{text: unsafe}]}}\n')
	with pytest.raises(flyerlib.render.FlyerError, match='page.margin must be 43.2'):
		flyerlib.render.build(unsafe_source, tmp_path / 'unsafe.pdf')
	source = tmp_path / 'balanced.yaml'
	source.write_text('''layout:
  col:
    gap: 0
    items:
      - qr: {url: https://example.com/top, size: 50}
      - qr: {url: https://example.com/bottom, size: 50}
''')
	output_path = tmp_path / 'balanced.pdf'
	flyerlib.render.build(source, output_path)
	page = pypdf.PdfReader(str(output_path)).pages[0]
	assert len(pypdf.PdfReader(str(output_path)).pages) == 1
	page_width = float(page.mediabox.width)
	page_height = float(page.mediabox.height)
	rectangles = [annotation.get_object()['/Rect'] for annotation in page['/Annots']]
	assert min(float(rectangle[1]) for rectangle in rectangles) == pytest.approx(43.2)
	assert max(float(rectangle[3]) for rectangle in rectangles) == pytest.approx(page_height - 43.2)
	for rectangle in rectangles:
		assert 43.2 <= float(rectangle[0]) <= page_width - 43.2
		assert 43.2 <= float(rectangle[2]) <= page_width - 43.2
