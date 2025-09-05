import pandas as pd
import cv2
import numpy as np
import os

# Load soil data
soil_data = pd.read_csv('data/soil_data.csv')
print(soil_data.head())

# Example: Load and preprocess land images
def load_images(image_dir):
    images = []
    for file in os.listdir(image_dir):
        if file.endswith('.jpg') or file.endswith('.png'):
            img = cv2.imread(os.path.join(image_dir, file))
            img = cv2.resize(img, (256, 256))  # Resize for model
            images.append(img)
    return np.array(images)

land_images = load_images('data/land_images/')
print("Loaded images:", land_images.shape)
