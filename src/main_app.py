import streamlit as st
import cv2
import numpy as np
import pickle
import tensorflow as tf
from preprocess import load_images
from visualization import visualize_land

# --------------------------
# Load Models
# --------------------------
@st.cache_resource
def load_segmentation_model():
    return tf.keras.models.load_model("models/segmentation_model.h5")

@st.cache_resource
def load_crop_model():
    with open("models/crop_prediction_model.pkl", "rb") as f:
        return pickle.load(f)

seg_model = load_segmentation_model()
crop_model = load_crop_model()

# --------------------------
# Streamlit UI
# --------------------------
st.title("🌾 AI-Based Crop Recommendation for Farmers")

# 1. Upload land image
uploaded_file = st.file_uploader("📤 Upload Land Image", type=['jpg','png'])
if uploaded_file:
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, channels="BGR", caption="Uploaded Land Image")

    # (Dummy segmentation prediction for demo)
    mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    mask[::2, ::2] = 1  # fake checkerboard just for visualization

    # Visualize segmented land
    segmented_img = visualize_land(image, mask)
    st.image(segmented_img, channels="RGB", caption="Segmented Land Map")

# 2. Soil input form
st.subheader("🧪 Enter Soil Data")
N = st.number_input("Nitrogen (N)", 0, 200, 90)
P = st.number_input("Phosphorus (P)", 0, 200, 40)
K = st.number_input("Potassium (K)", 0, 200, 40)
pH = st.number_input("pH", 0.0, 14.0, 6.5)
Moisture = st.number_input("Moisture (%)", 0, 100, 25)

if st.button("🔍 Recommend Crop"):
    features = np.array([[N, P, K, pH, Moisture]])
    prediction = crop_model.predict(features)[0]
    st.success(f"✅ Recommended Crop: **{prediction}**")
