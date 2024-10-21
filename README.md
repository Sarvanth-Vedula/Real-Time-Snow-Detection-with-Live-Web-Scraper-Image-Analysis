# Real-Time Snow Detection with Live Web Scraper

## Project Overview

This project is a real-time snow detection system that uses live images from a webcam located at Longs Peak in the Rocky Mountains. It detects snow in the images using a pre-trained machine learning model and sends notifications to alert users when snow is detected. 

## What This Project Does

- Scrapes images from a live webcam feed.
- Uses a machine learning model (ResNet50) to detect snow in the images.
- Sends real-time notifications to a mobile device using SimplePush when snow is detected.
- Allows testing on custom user-uploaded images as well.

## Technologies Used

- **Python**
- **TensorFlow/Keras** for the snow detection model (ResNet50).
- **Selenium** for web scraping live images.
- **SimplePush** for sending real-time notifications to mobile devices.
- **Streamlit** for dashboard display (optional).

## How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/Real-Time-Snow-Detection.git
cd Real-Time-Snow-Detection
```
### 2. Set Up the Virtual Environment
```bash
python3 -m venv tf_venv
source tf_venv/bin/activate  # On Windows, use tf_venv\Scripts\activate
```

### 3. Install the Dependencies
```bash
pip install -r requirements.txt
```

## 4. Set Up SimplePush for Notifications
- Create an account on SimplePush and get your API key.
- Update the real_time_alerts.py with your SimplePush API key.

### 5. Run the Project with Live Webcam Image Scraping
```bash
python3 main.py
```
