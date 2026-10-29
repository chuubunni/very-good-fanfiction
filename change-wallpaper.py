import ctypes
import requests
import os
from urllib.parse import urlparse
import sys


# img = "C:/Users/chuu/Documents/GitHub/very-good-fanfiction/THEimage.jpg"

# def automaticChange():
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)

# automaticChange()


def download_image(url, save_dir=os.getcwd()):
    """
    Downloads an image from the given URL and saves it locally.
    
    Args:
        url (str): The image URL.
        save_dir (str): Directory to save the image.
    
    Returns:
        str: Path to the saved image file.
    """
    try:
        # Validate URL
        parsed_url = urlparse(url)
        if not parsed_url.scheme.startswith("http"):
            raise ValueError("Invalid URL: Must start with http or https")

        # Create save directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)

        # Get image data
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL or generate one
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "THEimage.jpg"

        # Save image
        file_path = os.path.join(save_dir, filename)
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"Image successfully downloaded to: {file_path}")
        return file_path

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


def automaticChange(img):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)


# Example usage:
if __name__ == "__main__":
    # Replace with your AI-generated image URL
    image_url = "https://tfwiki.net/mediawiki/images2/3/36/MTMTE48_Sunder_face.jpg"
    img = download_image(image_url)
    automaticChange(img)