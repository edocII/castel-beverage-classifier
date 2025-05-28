# src/train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle
import os

# Load dataset
df = pd.read_csv('data/beverages.csv')

# Features and target
X = df[['Alcohol Content (%)', 'Sugar (g/L)', 'Bitterness (IBU)', 'Color (SRM)']]
y = df['Type']

# Encode target labels (Beer = 0, Spirit = 1, Cider = 2)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Save label encoder for later use
os.makedirs('models', exist_ok=True)
with open('models/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("Model and label encoder saved in 'models/' directory.")
