# LSB Matching Revisited Steganography Project

This project demonstrates how to encode and decode messages using the **LSB Matching Revisited** method of **Least Significant Bit (LSB) steganography**. This method improves upon traditional LSB steganography by reducing detectability and enhancing robustness through a matching technique. The hidden message can later be extracted and decoded from the image.

---

## Features

1. **Encode a Message**: Hide a secret message within an image using the LSB Matching Revisited technique.
2. **Decode a Message**: Extract the hidden message from an encoded image.
3. **Improved Robustness**: Enhances security by using the LSB Matching Revisited approach.

---

## Requirements

- Python 3.x
- `Pillow` library (for image manipulation)

Install the required library using:

```bash
pip install pillow

---

# LSB Matching Revisited Steganography Project

This project demonstrates how to encode and decode messages using the **LSB Matching Revisited** method of **Least Significant Bit (LSB) steganography**. This method improves upon traditional LSB steganography by reducing detectability and enhancing robustness through a matching technique. The hidden message can later be extracted and decoded from the image.

---

## Features

1. **Encode a Message**: Hide a secret message within an image using the LSB Matching Revisited technique.
2. **Decode a Message**: Extract the hidden message from an encoded image.
3. **Improved Robustness**: Enhances security by using the LSB Matching Revisited approach.

---

## Requirements

- Python 3.x
- `Pillow` library (for image manipulation)

Install the required library using:

```bash
pip install pillow
Usage
Encoding a Message into an Image
To encode a message into an image:

Run the script:

bash
Copy
Edit
python steganography.py
Follow the prompts:

Enter the image path: Provide the path of the image where the message will be hidden.
Enter the secret message: Input the message you want to encode.
Enter the output path: Provide the path where the new image (with the encoded message) will be saved.
Example:
plaintext
Copy
Edit
Enter the image path: input_image.png
Enter the secret message: This is a secret message.
Enter output image path: output_image.png
After execution, the encoded image will be saved as output_image.png.

Decoding a Message from an Image
To decode a hidden message from an image:

Run the script:

bash
Copy
Edit
python steganography.py
Follow the prompt:

Enter the image path: Provide the path of the image containing the hidden message.
Example:
plaintext
Copy
Edit
Enter the image path: output_image.png
The script will extract and display the hidden message.

How It Works
Encoding:

The secret message is converted into binary form.
The binary message is embedded into the least significant bits of the image’s pixel values using a matching approach to reduce changes to the pixel values.
Decoding:

The program extracts the least significant bits of the image’s pixel values.
It reconstructs the binary message and converts it back to text.
This method ensures minimal visual distortion of the original image and improves robustness against detection.
