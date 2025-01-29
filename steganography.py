import os
from PIL import Image

class Steganography:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size

    def encode(self, message, output_image_path):
        binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111111'
        binary_iter = iter(binary_message)

        for y in range(self.height):
            for x in range(self.width):
                pixel = list(self.pixels[x, y])
                for i in range(3):
                    try:
                        bit = next(binary_iter)
                        pixel[i] = pixel[i] & ~1 | int(bit)
                    except StopIteration:
                        self.pixels[x, y] = tuple(pixel)
                        self.image.save(output_image_path)
                        return
                self.pixels[x, y] = tuple(pixel)

    def decode(self):
        binary_message = ''

        for y in range(self.height):
            for x in range(self.width):
                pixel = self.pixels[x, y]
                for i in range(3):
                    binary_message += str(pixel[i] & 1)

        message_bits = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        message = ''
        for byte in message_bits:
            if byte == '11111111':
                break
            try:
                message += chr(int(byte, 2))
            except ValueError:
                print("Error decoding message: Invalid binary sequence.")
                return ''
        return message

def main():
    print("Steganography: LSB Matching Revisited")
    mode = input("Choose mode (encode/decode): ").strip().lower()

    if mode == "encode":
        image_path = input("Enter image path: ").strip()
        message = input("Enter the secret message: ").strip()
        output_path = input("Enter output image path: ").strip()

        if not os.path.exists(image_path):
            print("Error: Image path does not exist.")
            return

        stego = Steganography(image_path)
        stego.encode(message, output_path)
        print(f"Message encoded and saved to {output_path}")

    elif mode == "decode":
        image_path = input("Enter encoded image path: ").strip()

        if not os.path.exists(image_path):
            print("Error: Image path does not exist.")
            return

        stego = Steganography(image_path)
        decoded_message = stego.decode()

        if decoded_message:
            print(f"Decoded message: {decoded_message}")
        else:
            print("No valid message found.")

    else:
        print("Invalid mode. Choose 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
