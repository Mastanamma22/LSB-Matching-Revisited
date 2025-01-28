def validate_image(image_path: str):
    """Validate if the image exists and is a valid image."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    try:
        with Image.open(image_path) as img:
            img.verify()  # Verify if it's a valid image
    except Exception as e:
        raise ValueError(f"Invalid image file: {str(e)}")

def text_to_bin(text: str) -> str:
    """
    Converts text to a binary string.

    :param text: The text to convert.
    :return: A binary string representation of the text.
    """
    return ''.join(format(ord(c), '08b') for c in text)

def bin_to_text(binary: str) -> str:
    """
    Converts a binary string back to text.

    :param binary: The binary string to convert.
    :return: The decoded text.
    """
    chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)
