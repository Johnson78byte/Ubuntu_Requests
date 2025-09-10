import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def fetch_image():
    # Prompt user for image URL
    image_url = input("Enter the image URL: ").strip()

    # Validate URL format
    if not image_url.lower().startswith(('http://', 'https://')):
        print(" Invalid URL. Please enter a valid HTTP or HTTPS link.")
        return

    # Create directory if it doesn't exist
    save_dir = Path("Fetched_Images")
    save_dir.mkdir(exist_ok=True)

    try:
        # Attempt to download the image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        # Extract filename from URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        # Save image to directory
        file_path = save_dir / filename
        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"Image saved successfully as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {e}")

if __name__ == "__main__":
    fetch_image()
