# src/predict.py

import pickle
import numpy as np

# Load model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load label encoder
with open('models/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Prompt user for input features
print("\n🔍 Enter beverage features to classify:")
alcohol = float(input("Alcohol Content (%) → "))
sugar = float(input("Sugar (g/L) → "))
bitterness = float(input("Bitterness (IBU) → "))
color = float(input("Color (SRM) → "))

# Prepare input for prediction
sample = np.array([[alcohol, sugar, bitterness, color]])

# Predict
predicted_class = model.predict(sample)[0]
predicted_label = label_encoder.inverse_transform([predicted_class])[0]

print(f"\n✅ Predicted Beverage Type: {predicted_label}")
