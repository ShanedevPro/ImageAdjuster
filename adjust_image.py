"""
adjust_image.py: Resizes and changes the format of images according to user-defined parameters.
"""

from PIL import Image
import sys
import io
import argparse


def adjust_image(file_path, min_width, min_height, output_format, min_size_kb, max_size_kb):
    """
    Adjusts an image according to user specifications:
    - Minimum resolution
    - Output file format
    - File size range
    """
    # Load the image
    with Image.open(file_path) as img:
        print(f"Original image size: {img.size}, Format: {img.format}")

        # Ensure minimum resolution
        if img.width < min_width or img.height < min_height:
            aspect_ratio = img.width / img.height
            new_width = max(min_width, int(min_height * aspect_ratio))
            new_height = max(min_height, int(new_width / aspect_ratio))
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            print(f"Image resized to: {img.size}")

        # Convert to desired format
        if output_format.lower() == 'jpg':
            img = img.convert("RGB")

        # Adjust file size by tweaking the quality
        for quality in range(95, 10, -5):
            with io.BytesIO() as buffer:
                img.save(buffer, format=output_format.upper(), quality=quality)
                size_kb = buffer.tell() / 1024
                if min_size_kb <= size_kb <= max_size_kb:
                    output_path = file_path.rsplit(".", 1)[0] + f"_adjusted.{output_format.lower()}"
                    with open(output_path, "wb") as f:
                        f.write(buffer.getvalue())
                    print(f"Image saved as '{output_path}' with quality={quality}, Size={size_kb:.2f}KB")
                    return
        print("Warning: Couldn't adjust the image size within the desired range.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adjust image resolution, format, and size.")
    parser.add_argument("file_path", help="Path to the input image file")
    parser.add_argument("--width", type=int, default=360, help="Minimum width in pixels")
    parser.add_argument("--height", type=int, default=480, help="Minimum height in pixels")
    parser.add_argument("--format", type=str, default="jpg", choices=["jpg", "png"], help="Output image format")
    parser.add_argument("--min_size", type=int, default=20, help="Minimum file size in KB")
    parser.add_argument("--max_size", type=int, default=200, help="Maximum file size in KB")

    args = parser.parse_args()

    adjust_image(
        file_path=args.file_path,
        min_width=args.width,
        min_height=args.height,
        output_format=args.format,
        min_size_kb=args.min_size,
        max_size_kb=args.max_size
    )
