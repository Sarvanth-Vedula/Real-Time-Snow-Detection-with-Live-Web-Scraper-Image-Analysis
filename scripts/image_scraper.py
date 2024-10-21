from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
from datetime import datetime
import os
from datetime import datetime

# Path to your ChromeDriver
CHROME_DRIVER_PATH = '/Users/sarvanthvedula/Downloads/chromedriver-mac-arm64 2/chromedriver'

# The URL of the website with the live webcam image
WEBPAGE_URL = "https://www.nps.gov/media/webcam/view.htm?id=81B46847-1DD8-B71B-0B46D032F33B54DF"

def get_latest_image_url():
    """
    Use Selenium to load the website and extract the dynamic image URL.
    """
    # Initialize the Chrome browser (headless mode)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    
    # Load the webpage
    driver.get(WEBPAGE_URL)
    
    # Wait for the image to load
    time.sleep(5)  # Give the page some time to load
    
    try:
        # Find the image element by its ID and extract the "src" attribute
        img_element = driver.find_element(By.ID, "webcamRefreshImage")
        img_url = img_element.get_attribute("src")
        driver.quit()
        return img_url
    except Exception as e:
        print(f"Error retrieving image URL: {e}")
        driver.quit()
        return None

def download_image(image_url):
    """
    Downloads the live webcam image from the specified URL and saves it to the 'images' directory.
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Timestamp for image filename
    image_dir = 'images'  # Save images to the images/ folder

    # Create directory if it doesn't exist
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    image_path = os.path.join(image_dir, f"longs_peak_{timestamp}.jpg")

    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, "wb") as file:
                file.write(response.content)
                print(f"Image downloaded: {image_path}")
            return image_path
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def run_image_scraper():
    """
    Runs the image scraper every 1 minute.
    """
    while True:
        image_url = get_latest_image_url()  # Get the latest image URL dynamically
        if image_url:
            download_image(image_url)  # Download the latest image
        time.sleep(60)  # Wait for 1 minute before the next download

if __name__ == "__main__":
    run_image_scraper()
