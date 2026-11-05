#!/usr/bin/env python3
"""Capture the live Voss Lab GitHub contribution graph in light mode."""
import pathlib
import random
import subprocess
import tempfile
import time

import PIL.Image
import playwright.sync_api


def repository_root() -> pathlib.Path:
	script_directory = pathlib.Path(__file__).resolve().parent
	result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=script_directory,
		check=True, capture_output=True, text=True)
	root = pathlib.Path(result.stdout.strip())
	return root


def capture_graph(output_path: pathlib.Path) -> None:
	"""Save GitHub's loaded light-mode graph as a quality-95 WebP image."""
	with tempfile.TemporaryDirectory() as temporary_directory:
		temporary_path = pathlib.Path(temporary_directory)
		png_path = temporary_path / 'contribution_graph.png'
		webp_path = temporary_path / 'contribution_graph.webp'
		with playwright.sync_api.sync_playwright() as browser_api:
			browser = browser_api.chromium.launch()
			page = browser.new_page(viewport={'width': 1440, 'height': 1100}, device_scale_factor=4,
				color_scheme='light')
			time.sleep(random.random())
			page.goto('https://github.com/vosslab', wait_until='domcontentloaded')
			page.evaluate("""
				document.documentElement.setAttribute('data-color-mode', 'light');
				document.documentElement.setAttribute('data-light-theme', 'light');
				document.documentElement.setAttribute('data-dark-theme', 'light');
			""")
			calendar = page.locator('.js-calendar-graph')
			calendar.wait_for(state='visible')
			page.wait_for_function("document.querySelectorAll('.ContributionCalendar-day[data-date]').length >= 300")
			cell_count = calendar.locator('.ContributionCalendar-day[data-date]').count()
			if cell_count < 300:
				raise RuntimeError(f'GitHub contribution graph has only {cell_count} dated cells')
			background_color = page.locator('body').evaluate("element => getComputedStyle(element).backgroundColor")
			if background_color != 'rgb(255, 255, 255)':
				raise RuntimeError(f'GitHub profile did not render with a white light-mode background: {background_color}')
			calendar.screenshot(path=str(png_path))
			browser.close()
		with PIL.Image.open(png_path) as image:
			image.save(webp_path, 'WEBP', quality=95, method=6)
		webp_path.replace(output_path)


def main() -> None:
	root = repository_root()
	output_path = root / 'flyers' / 'github' / 'assets' / 'contribution_graph.webp'
	capture_graph(output_path)
	print(output_path)


if __name__ == '__main__':
	main()
