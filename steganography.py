import os
from PIL import Image

class LSBSteganography:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path).convert("RGB")
        self.pixels = self.image.load()

    def encode(self, message, output_image_path):
        # Convert the message to binary and append a null terminator
        binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'
        message_index = 0
        width, height = self.image.size

        for y in range(height):
            for x in range(width):
                if message_index < len(binary_message):
                    r, g, b = self.pixels[x, y]

                    # Modify the LSBs of R, G, and B channels
                    r = (r & ~1) | int(binary_message[message_index])
                    message_index += 1

                    if message_index < len(binary_message):
                        g = (g & ~1) | int(binary_message[message_index])
                        message_index += 1

                    if message_index < len(binary_message):
                        b = (b & ~1) | int(binary_message[message_index])
                        message_index += 1

                    self.pixels[x, y] = (r, g, b)

        # Save the encoded image as PNG to avoid compression artifacts
        self.image.save(output_image_path, format="PNG")
        print("Message successfully encoded.")

    def decode(self):
        binary_message = ''
        width, height = self.image.size

        for y in range(height):
            for x in range(width):
                r, g, b = self.pixels[x, y]
                binary_message += str(r & 1)
                binary_message += str(g & 1)
                binary_message += str(b & 1)

                # Check for null terminator every 8 bits
                if len(binary_message) >= 8 and binary_message[-8:] == '00000000':
                    binary_message = binary_message[:-8]  # Remove null terminator
                    break
            else:
                continue
            break

        # Ensure the binary_message length is a multiple of 8
        if len(binary_message) % 8 != 0:
            binary_message = binary_message[:len(binary_message) - (len(binary_message) % 8)]

        try:
            # Convert binary message to string
            decoded_message = ''.join(
                chr(int(binary_message[i:i + 8], 2))
                for i in range(0, len(binary_message), 8)
            )

            if '\x00' in decoded_message:
                decoded_message = decoded_message[:decoded_message.index('\x00')]

            return decoded_message if decoded_message else "Error: No valid message found or the image is not encoded."
        except ValueError:
            return "Error: Decoding failed due to invalid binary data."


def main():
    print("Steganography: LSB Matching Revisited")
    mode = input("Choose mode (encode/decode): ").strip().lower()

    if mode == "encode":
        image_path = input("Enter image path: ").strip()
        if not os.path.exists(image_path):
            print("Error: Image file does not exist.")
            return

        message = input("Enter message to encode: ").strip()
        output_image_path = input("Enter output image path: ").strip()

        stego = LSBSteganography(image_path)
        stego.encode(message, output_image_path)

    elif mode == "decode":
        encoded_image_path = input("Enter encoded image path: ").strip()
        if not os.path.exists(encoded_image_path):
            print("Error: Encoded image file does not exist.")
            return

        stego = LSBSteganography(encoded_image_path)
        message = stego.decode()
        print(f"Decoded message: {message}")

    else:
        print("Invalid mode. Please choose 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
