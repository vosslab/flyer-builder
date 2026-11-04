import pathlib

import pypdf

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
