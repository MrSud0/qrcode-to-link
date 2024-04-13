import sys
import cv2
from pyzbar.pyzbar import decode
from urllib.parse import urlparse

def is_url(url):
    """
    Check if the provided string is a valid URL.

    Parameters:
        url (str): The string to check for URL validity.

    Returns:
        bool: True if the string is a valid URL, False otherwise.
    """
    try:
        result = urlparse(url)
        # Check if the scheme and netloc are present
        return all([result.scheme, result.netloc])
    except:
        return False

def read_qr_code_from_file(image_path):
    """
    Read and decode a QR code from an image file.

    Parameters:
        image_path (str): The path to the image file to read.

    Returns:
        None: Outputs the decoded data to the console.
    """
    # Load the image
    img = cv2.imread(image_path)

    # Check if the image is loaded
    if img is None:
        print("Error: Image could not be read.")
        return

    # Decode the QR code
    decoded_objects = decode(img)
    if decoded_objects:
        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            if is_url(data):
                print("URL found:", data)
            else:
                print("Data found:", data)
    else:
        print("No QR Code found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python qr_code_reader_file.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    read_qr_code_from_file(image_path)
