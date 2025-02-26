import cv2
import numpy as np

def encode_LSB(image_path, output_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    full_message = password + ":" + message + "~"  # Add an end marker
    binary_message = ''.join(format(ord(char), '08b') for char in full_message)
    msg_len = len(binary_message)

    n, m, z, bit_index = 0, 0, 0, 0

    if msg_len > img.shape[0] * img.shape[1] * 3:
        print("Error: Message is too long for this image!")
        return

    for bit in binary_message:
        img[n, m, z] = (img[n, m, z] & 254) | int(bit)  # Modify LSB only
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    cv2.imwrite(output_path, img)
    print(f"Message encoded using LSB steganography! Saved as {output_path}")

if __name__ == "__main__":
    image_path = "normal_dog_image.jpg"  # Use PNG for lossless compression
    output_path = "stego_dog_image.png"
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encode_LSB(image_path, output_path, message, password)
