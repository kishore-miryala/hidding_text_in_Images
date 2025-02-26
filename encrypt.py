import cv2

def encrypt_image(image_path, output_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    d = {chr(i): i for i in range(255)}
    full_message = password + ":" + message + "~"  # Add "~" as an end marker
    msg_len = len(full_message)
    n, m, z = 0, 0, 0
    if msg_len > img.shape[0] * img.shape[1] * 3:
        print("Error: Message is too long for this image!")
        return

    for i in range(msg_len):
        img[n, m, z] = d[full_message[i]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
    cv2.imwrite(output_path, img)
    print(f"Message encrypted successfully! Saved as {output_path}")

if __name__ == "__main__":
    image_path = "normal_dog_image.jpg"  # Use PNG for lossless encryption
    output_path = "stego_dog_image.png"
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypt_image(image_path, output_path, message, password)
