# ImageAdjuster

ImageAdjuster is a small Python CLI that resizes images, converts between JPG and PNG, and searches for an output quality that lands inside a target file-size range.

## What It Does

- Upscales images that are smaller than your minimum width or height requirements
- Converts output to `jpg` or `png`
- Iterates over quality settings to try to fit the output into a desired size window
- Writes the adjusted image next to the original file with an `_adjusted` suffix

## Tech Stack

- Python
- Pillow

## Installation

```bash
git clone https://github.com/ShanedevPro/ImageAdjuster.git
cd ImageAdjuster
pip install -r requirements.txt
```

## Quick Start

```bash
python adjust_image.py ./input/photo.png
```

This uses the default rules:

- minimum width: `360`
- minimum height: `480`
- output format: `jpg`
- file size target: `20 KB` to `200 KB`

## Examples

### Resize and convert to JPG

```bash
python adjust_image.py ./input/photo.png --width 800 --height 600 --format jpg
```

### Keep PNG output and narrow the file-size window

```bash
python adjust_image.py ./input/photo.png --format png --min_size 80 --max_size 120
```

## Current Limitations

- The tool increases image size when the source image is smaller than the target minimum resolution.
- It only supports `jpg` and `png` outputs.
- If no quality setting can satisfy the requested size range, the script prints a warning instead of forcing an output.

## Output Behavior

If the input file is `photo.png`, the adjusted file is written as:

```text
photo_adjusted.jpg
```

or

```text
photo_adjusted.png
```

depending on the selected output format.

## License

MIT
