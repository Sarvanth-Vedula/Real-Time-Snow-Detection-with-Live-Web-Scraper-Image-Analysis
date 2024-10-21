import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from scripts.real_time_alerts import send_simplepush_notification  # Import the SimplePush notification function

def load_snow_model(model_path="models/snow_detection_model.keras"):
    """
    Load the pre-trained snow detection model.
    """
    if os.path.exists(model_path):
        return load_model(model_path)
    else:
        raise FileNotFoundError(f"Model file not found at {model_path}")

def preprocess_image(img_path, target_size=(224, 224)):
    """
    Preprocess the image for snow detection.
    """
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image to [0, 1]
    return img_array

def is_snowing(img_path, model):
    """
    Predict if the image contains snow using the trained model.
    """
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)
    return prediction[0][0] > 0.5  # True if snow is detected

def run_snow_detection(image_path):
    """
    Run the snow detection on the latest image.
    """
    try:
        model = load_snow_model()  # Load the saved model
        if os.path.exists(image_path):
            if is_snowing(image_path, model):
                print("It is snowing in the latest image!")
                send_simplepush_notification("Hi4g6F", "Snow Alert", "It is snowing at Longs Peak!")  # API key must be in quotes
                return True  # Snow detected
            else:
                print("No snow detected in the latest image.")
                send_simplepush_notification("Hi4g6F", "No Snow Alert", "No snow detected at Longs Peak.")  # API key must be in quotes
                return False  # No snow
        else:
            print(f"No image found at {image_path}.")
            return None
    except Exception as e:
        print(f"Error running snow detection: {e}")
        return None
    
# # New method to allow custom image upload and processing
# def run_snow_detection_custom(image_path):
#     """
#     Run snow detection on a custom image provided by the user.
#     """
#     try:
#         model = load_snow_model()  # Load the saved model
#         if os.path.exists(image_path):
#             if is_snowing(image_path, model):
#                 print(f"Snow detected in the custom image: {image_path}")
#                 send_simplepush_notification("Hi4g6F", "Snow Alert", "Snow detected in the custom image!")
#                 return True  # Snow detected
#             else:
#                 print(f"No snow detected in the custom image: {image_path}")
#                 send_simplepush_notification("Hi4g6F", "No Snow Alert", "No snow detected in the custom image.")
#                 return False  # No snow
#         else:
#             print(f"Custom image not found at {image_path}.")
#             return None
#     except Exception as e:
#         print(f"Error running snow detection on custom image: {e}")
#         return None
