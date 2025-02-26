import cv2

def decrypt_image(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    c = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    extracted_data = ""
    try:
        while True:
            char = c.get(img[n, m, z], None)
            if char is None or char == "~":  # Stop at end marker "~"
                break
            extracted_data += char
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= img.shape[1]:
                    m = 0
                    n += 1
    except IndexError:
        print("Warning: Reached image boundary before full extraction.")
    if ":" not in extracted_data:
        print("Error: Unable to find password separator. Message might be corrupted.")
        return
    stored_pass, message = extracted_data.split(":", 1)
    if password == stored_pass:
        print("Decryption successful! Message:", message)
    else:
        print("ERROR: Incorrect password!")

if __name__ == "__main__":
    image_path = "stego_dog_image.png"
    password = input("Enter passcode for decryption: ")
    decrypt_image(image_path, password)
