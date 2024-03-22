
# ImageAdjuster

## Project Overview

ImageAdjuster is a Python tool designed to adjust images according to user-defined specifications. It allows users to resize images, change their format, and adjust the compression quality to meet various requirements. This project utilizes the Pillow library for image processing tasks.

## Features

- **Resize Images:** Change the dimensions of an image to specified width and height.
- **Format Conversion:** Convert images to different formats (e.g., JPEG, PNG).
- **Quality Adjustment:** Modify the compression quality of images, useful for reducing file size.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/ImageAdjuster.git
cd ImageAdjuster
```

2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

## Usage

To use ImageAdjuster, run the `adjust_image.py` script with the desired parameters. Below are some examples of common operations.

### Resize an Image

```bash
python adjust_image.py --path /path/to/image.jpg --width 800 --height 600
```

### Convert Image Format

```bash
python adjust_image.py --path /path/to/image.png --format JPEG
```

### Adjust Image Quality

```bash
python adjust_image.py --path /path/to/image.jpg --quality 85
```

## Contributing

Contributions to ImageAdjuster are welcome! If you're interested in helping improve this tool, please take a look at our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to submit issues, feature requests, and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

