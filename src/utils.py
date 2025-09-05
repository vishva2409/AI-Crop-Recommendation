import pandas as pd
import numpy as np
import os

# -----------------------------
# CSV / Data helpers
# -----------------------------
def load_soil_data(path="data/soil_data.csv"):
    """Load soil data CSV as pandas DataFrame"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Soil data not found at {path}")
    return pd.read_csv(path)

def load_crop_data(path="data/crop_data.csv"):
    """Load crop reference data CSV as pandas DataFrame"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Crop data not found at {path}")
    return pd.read_csv(path)

# -----------------------------
# Image helpers
# -----------------------------
def normalize_image(img_array):
    """Normalize image array to 0-1 range"""
    return img_array / 255.0

def resize_image(img, size=(256,256)):
    """Resize PIL image to target size"""
    from PIL import Image
    return img.resize(size)

# -----------------------------
# Utility functions
# -----------------------------
def ensure_dir(path):
    """Create directory if it does not exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def one_hot_encode_mask(mask, num_classes):
    """Convert a 2D mask to one-hot encoding"""
    return np.eye(num_classes)[mask]
