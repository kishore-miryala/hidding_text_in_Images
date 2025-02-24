# Image Steganography - Hide and Retrieve Secret Messages in Images
This project demonstrates the technique of **image steganography**, which involves hiding secret information within an image in such a way that the existence of the information is concealed. The primary goal is to enable secure communication by embedding messages into digital images without altering their visible properties.

## Features
**Hide Text Messages:** Embed secret text messages within an image file.  
**Extract Hidden Messages:** Retrieve and display hidden messages from an image file.  
**Simple User Interface:** A straightforward interface to encode and decode messages.  
## Requirements
- Python 3.x  
- CV2 library  
Install the Cv2 library using pip:  
```shell
pip install -r requirements.txt -y
```
## Usage
### Encoding a Message:

Run the `encode.py` script.
Input the path to the cover image (e.g., normal_cat_image.jpg).
Enter the secret message you wish to hide.
Specify the output image file name (e.g., stego_cat_image.jpg).
The script will embed the secret message into the specified image and save the resulting stego image.

### Decoding a Message:

Run the `decode.py` script.
Input the path to the stego image (e.g., stego_cat_image.png).
The script will extract and display the hidden message from the image.

## How It Works
The project utilizes the Least Significant Bit (LSB) technique for steganography. In this method, the least significant bits of the image's pixel values are modified to encode the bits of the secret message. Since changes in the LSBs have a minimal impact on the overall appearance of the image, the hidden message remains imperceptible to the human eye.

## Limitations
The size of the secret message is limited by the dimensions and color depth of the cover image.
The current implementation does not support encryption; the hidden message is not encrypted within the image.
License
This project is licensed under the MIT License.

