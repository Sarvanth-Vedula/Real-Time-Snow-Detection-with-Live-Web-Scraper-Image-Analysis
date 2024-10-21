import requests
import os

def send_simplepush_notification(api_key, title, message):
    """
    Sends a push notification via SimplePush.
    """
    # Create the URL dynamically based on the message passed
    url = f'https://api.simplepush.io/send/{api_key}/{title}/{message}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Notification sent successfully!")
        else:
            print(f"Failed to send notification. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending notification: {e}")

def display_dashboard(image_path, result):
    """
    Display the latest image and result on a simple web dashboard using Streamlit.
    """
    import streamlit as st
    from PIL import Image

    st.title("Real-Time Snow Detection")
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, caption="Latest Image from Longs Peak")

        if result:
            st.write("It is snowing!")
        else:
            st.write("No snow detected.")
    else:
        st.write("No image available.")
