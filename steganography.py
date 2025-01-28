import os
from PIL import Image
from utils import validate_image, text_to_bin, bin_to_text

class LSBSteganography:
    def __init__(self, image_path: str):
        """
        Initializes the LSB Steganography with the given image path.

        :param image_path: Path to the image file.
        """
        self.image_path = image_path
        self.image = None

    def load_image(self):
        """Load the image into the program."""
        try:
            self.image = Image.open(self.image_path)
        except Exception as e:
            raise ValueError(f"Error loading image: {str(e)}")

    def encode(self, message: str, output_image_path: str):
        """
        Encodes the message into the image using LSB.

        :param message: The secret message to encode.
        :param output_image_path: Path to save the image with the encoded message.
        """
        if not self.image:
            self.load_image()

        message_bin = text_to_bin(message)
        message_len = len(message_bin)
        width, height = self.image.size
        pixels = self.image.load()

        if message_len > width * height:
            raise ValueError("Message too large for this image.")

        msg_index = 0
        for y in range(height):
            for x in range(width):
                pixel = list(pixels[x, y])

                for color_index in range(3):  # RGB channels
                    if msg_index < message_len:
                        pixel[color_index] = (pixel[color_index] & ~1) | int(message_bin[msg_index])
                        msg_index += 1
                    if msg_index >= message_len:
                        break

                pixels[x, y] = tuple(pixel)

                if msg_index >= message_len:
                    break
            if msg_index >= message_len:
                break

        self.image.save(output_image_path)
        print(f"Message encoded and saved to {output_image_path}")

    def decode(self):
        """
        Decodes the hidden message from the image.

        :return: The decoded message.
        """
        if not self.image:
            self.load_image()

        width, height = self.image.size
        pixels = self.image.load()

        message_bin = ""
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]

                for color_index in range(3):  # RGB channels
                    message_bin += str(pixel[color_index] & 1)

        # Convert binary to text
        return bin_to_text(message_bin)

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    stego = LSBSteganography(image_path)

    action = input("Do you want to encode or decode a message? (e/d): ").strip().lower()
    if action == 'e':
        message = input("Enter the secret message: ")
        output_image_path = input("Enter output image path: ")
        stego.encode(message, output_image_path)
    elif action == 'd':
        decoded_message = stego.decode()
        print(f"Decoded message: {decoded_message}")
    else:
        print("Invalid action.")
