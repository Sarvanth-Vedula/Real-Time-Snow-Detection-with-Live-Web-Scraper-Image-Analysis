import os
from scripts.image_scraper import download_image, get_latest_image_url
from scripts.snow_detection import run_snow_detection
# from scripts.snow_detection import run_snow_detection_custom
import time

def main():
    """
    The main loop to continuously download images, detect snow, and send alerts.
    """
    while True:
        # Get the latest image URL dynamically
        image_url = get_latest_image_url()

        if image_url:
            # Download the image using the extracted image URL
            image_path = download_image(image_url)

            if image_path:
                # Run snow detection and send notifications
                run_snow_detection(image_path)

        # Wait for 1 minute before the next check
        time.sleep(60)
        
# def test_custom_image():
#     """
#     Function to test custom uploaded images for snow detection.
#     """
#     custom_image_path = '/Users/sarvanthvedula/Downloads/test.jpg'  # Update this with the path to your custom image
#     run_snow_detection_custom(custom_image_path)  # Call the custom image detection function
    
    
if __name__ == "__main__":
    main()
    # test_custom_image()

