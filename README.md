# AI Crop Recommendation System

--> AI Crop Recommendation System is a machine learning-based project designed to help farmers choose suitable crops based on soil and environmental conditions. The system takes soil parameters such as Nitrogen, Phosphorus, Potassium, pH, and Moisture as input and recommends the most suitable crop using a trained machine learning model.

## Project Overview

--> Agriculture plays an important role in food production, but choosing the right crop for a particular land area can be difficult without proper soil knowledge.
This project uses Artificial Intelligence and Machine Learning to support crop selection by analyzing soil-related data.

--> The project also includes land image processing and segmentation-related modules to support visual analysis of agricultural land.

## Features

- Crop recommendation based on soil parameters
- Soil nutrient analysis
- Land image upload using Streamlit
- Image preprocessing for land images and masks
- Basic land segmentation model structure
- Visualization of segmented land area
- Machine learning model training using Random Forest

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- OpenCV
- TensorFlow / Keras
- Matplotlib
- PIL

## Project Structure

AI-Crop-Recommendation/
│
├── data/
│   ├── crop_data.csv
│   ├── soil_data.csv
│   └── land_images/
│
├── src/
│   ├── main_app.py
│   ├── train_crop_model.py
│   ├── soil_analysis.py
│   ├── preprocess.py
│   ├── preprocess_images.py
│   ├── train_segmentation.py
│   ├── visualization.py
│   ├── utils.py
│   ├── make_pairs_csv.py
│   └── split_dataset.py
│
├── requirements.txt
└── README.md
