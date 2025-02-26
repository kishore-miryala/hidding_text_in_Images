import cv2
import numpy as np

def decode_LSB(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    binary_message = ""
    n, m, z = 0, 0, 0

    try:
        while True:
            binary_message += str(img[n, m, z] & 1)  # Extract LSB
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= img.shape[1]:
                    m = 0
                    n += 1
            if len(binary_message) % 8 == 0 and len(binary_message) > 0:
                char = chr(int(binary_message[-8:], 2))  # Convert from binary to char
                if char == "~":  # Stop at end marker
                    break
    except IndexError:
        print("Warning: Reached image boundary before full extraction.")

    extracted_data = "".join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    if ":" not in extracted_data:
        print("Error: Unable to find password separator. Message might be corrupted.")
        return

    stored_pass, message = extracted_data.split(":", 1)
    message = message.rstrip("~")  # Remove the trailing "~"

    if password == stored_pass:
        print("Decryption successful! Message:", message)
    else:
        print("ERROR: Incorrect password!")

if __name__ == "__main__":
    image_path = "stego_dog_image.png"
    password = input("Enter passcode for decryption: ")
    decode_LSB(image_path, password)
