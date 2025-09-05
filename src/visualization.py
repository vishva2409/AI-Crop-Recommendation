import matplotlib.pyplot as plt
import numpy as np
import cv2

def visualize_land(land_image, segmentation_mask):
    color_map = {
        0: [0,255,0],   # Crop1 - Green
        1: [0,0,255],   # Crop2 - Blue
        2: [255,0,0]    # Crop3 - Red
    }
    overlay = np.zeros_like(land_image)
    for i in range(segmentation_mask.shape[0]):
        for j in range(segmentation_mask.shape[1]):
            overlay[i,j] = color_map[segmentation_mask[i,j]]
    result = cv2.addWeighted(land_image, 0.6, overlay, 0.4, 0)
    plt.imshow(result)
    plt.show()
