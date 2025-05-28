# Castel Malawi Beverage Classifier 🍻🇲

A simple machine learning project that classifies beverages produced by **Castel Malawi Ltd** into categories: **Beer**, **Spirit**, or **Cider**, based on features like alcohol content, sugar level, bitterness, and color.

This project uses Scikit-learn and runs entirely from the command line (CLI).

---

## 🔍 Features

- Trains a Random Forest classifier on a custom beverage dataset
- Predicts beverage type based on 4 chemical/visual features
- Uses products and data from Castel Malawi Ltd 
(synthetic data from **Castel Malawi Ltd**) 
- All Rights Reserved. © Copyright 2025 **Castel Malawi Ltd**
- CLI-only, no web interface required

---

## 📂 Project Structure

castel-beverage-classifier/
├── data/
│ └── beverages.csv # Synthetic beverage dataset
├── src/
│ ├── train.py # Train model
│ └── predict.py # Predict using trained model
├── models/
│ ├── model.pkl # Saved ML model
│ └── label_encoder.pkl # Saved label encoder
├── requirements.txt # Dependencies
├── README.md # Project instructions
└── .gitignore # Ignore Python cache & models


---

## 🚀 How to Use

### 1. Install requirements

```bash
pip install -r requirements.txt


### 2. Train the model type into the bash
python src/train.py


3. Predict a beverage type into the bash

python src/predict.py

You’ll be prompted to enter:

    Alcohol Content (%) ->

    Sugar (g/L) ->

    Bitterness (IBU) ->

    Color (SRM) ->

Then you’ll get a prediction like in python: ✅ Predicted Beverage Type: Beer

Sample Dataset
Stored in data/beverages.csv, using synthetic values for:

    Kuche Kuche

    Carlsberg Green

    Malawi Gin

    Premier Brandy

    Pomme Breeze

    and more..

✅ Status

✔️ Complete, ready to run
🧪 Can be improved with a real dataset
🌍 Focused on local Malawian beverages

