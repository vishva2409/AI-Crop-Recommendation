import os
from PIL import Image
import numpy as np

INPUT_IMG_DIR = "data/land_images"
INPUT_MASK_DIR = "data/masks"
OUT_DIR = "data/preprocessed"
IMG_SIZE = (256, 256)

os.makedirs(os.path.join(OUT_DIR, "images"), exist_ok=True)
os.makedirs(os.path.join(OUT_DIR, "masks"), exist_ok=True)

def preprocess():
    img_files = [f for f in os.listdir(INPUT_IMG_DIR) if f.lower().endswith(('.jpg','.png','.jpeg'))]
    for fname in img_files:
        img_path = os.path.join(INPUT_IMG_DIR, fname)
        mask_path = os.path.join(INPUT_MASK_DIR, os.path.splitext(fname)[0] + ".png")

        img = Image.open(img_path).convert("RGB").resize(IMG_SIZE)
        Image.fromarray(np.array(img)).save(os.path.join(OUT_DIR,"images", fname))

        if os.path.exists(mask_path):
            mask = Image.open(mask_path).convert("L").resize(IMG_SIZE, resample=Image.NEAREST)
            Image.fromarray(np.array(mask)).save(os.path.join(OUT_DIR,"masks", os.path.splitext(fname)[0] + ".png"))
        else:
            print("⚠️ Warning: mask not found for", fname)

if __name__ == "__main__":
    preprocess()
    print("✅ Preprocessing done")
