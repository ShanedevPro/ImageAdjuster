"""
adjust_image.py: Resizes and changes the format of images according to user-defined parameters.
"""

from PIL import Image
import io
import argparse


JPEG_FORMATS = {"jpg", "jpeg"}


def get_resample_filter():
    if hasattr(Image, "Resampling"):
        return Image.Resampling.LANCZOS
    return Image.LANCZOS


def normalize_output_format(output_format):
    normalized = output_format.lower()
    if normalized in JPEG_FORMATS:
        return "JPEG", "jpg"
    if normalized == "png":
        return "PNG", "png"
    raise ValueError(f"Unsupported output format: {output_format}")


def save_with_target_size(img, normalized_format, min_size_kb, max_size_kb):
    if normalized_format == "JPEG":
        for quality in range(95, 10, -5):
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=quality, optimize=True)
            size_kb = buffer.tell() / 1024
            if min_size_kb <= size_kb <= max_size_kb:
                return buffer.getvalue(), quality, size_kb
        return None, None, None

    for compression_level in range(9, -1, -1):
        buffer = io.BytesIO()
        img.save(
            buffer,
            format="PNG",
            optimize=True,
            compress_level=compression_level,
        )
        size_kb = buffer.tell() / 1024
        if min_size_kb <= size_kb <= max_size_kb:
            return buffer.getvalue(), compression_level, size_kb
    return None, None, None


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
        normalized_format, output_extension = normalize_output_format(output_format)

        # Ensure minimum resolution
        if img.width < min_width or img.height < min_height:
            aspect_ratio = img.width / img.height
            new_width = max(min_width, int(min_height * aspect_ratio))
            new_height = max(min_height, int(new_width / aspect_ratio))
            img = img.resize((new_width, new_height), get_resample_filter())
            print(f"Image resized to: {img.size}")

        # Convert to desired format
        if normalized_format == "JPEG":
            img = img.convert("RGB")

        image_bytes, setting_value, size_kb = save_with_target_size(
            img,
            normalized_format,
            min_size_kb,
            max_size_kb,
        )
        if image_bytes is not None:
            output_path = file_path.rsplit(".", 1)[0] + f"_adjusted.{output_extension}"
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            setting_label = "quality" if normalized_format == "JPEG" else "compress_level"
            print(
                f"Image saved as '{output_path}' with {setting_label}={setting_value}, "
                f"Size={size_kb:.2f}KB"
            )
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
