#!/usr/bin/env python3
"""Build one coordinate-free flyer YAML document as a PDF."""
import argparse
import pathlib

import flyerlib.render


def parse_args() -> argparse.Namespace:
	"""Parse command line arguments."""
	parser = argparse.ArgumentParser(description='Build a one-page flyer PDF from YAML.')
	parser.add_argument('-i', '--input', dest='input_file', required=True, help='Flyer YAML file')
	parser.add_argument('-o', '--output', dest='output_file', help='PDF output path')
	return parser.parse_args()


def main() -> None:
	"""Build the selected flyer."""
	args = parse_args()
	input_path = pathlib.Path(args.input_file)
	output_path = pathlib.Path(args.output_file) if args.output_file else pathlib.Path('output/pdf') / (input_path.stem + '.pdf')
	flyerlib.render.build(input_path, output_path)
	print(output_path)


if __name__ == '__main__':
	main()
