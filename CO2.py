import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Data Loading and Initial Exploration
# Read the data from a CSV file
data = pd.read_csv('CO2 Emissions_Canada.csv', encoding='ISO-8859-1')

# Optionally, explore the data to understand its structure and quality
# Data exploration and preprocessing steps can be added here

# Step 2: Data Preprocessing (if needed)
# Data preprocessing (cleaning, handling missing values, etc.) can be added here

# Step 3: Define Predictor Variables (X) and Target Variable (y)
# Example: Using multiple predictors for CO2 emissions
X = data[['Engine Size', 'Feature2', 'Feature3', 'Feature4', 'Feature5']]
y = data['CO2 Emissions(g/km)']

# Step 4: Create and Fit a Multiple Linear Regression Model
reg_model = LinearRegression()
reg_model.fit(X, y)

# Step 5: Make Predictions
# Predict CO2 emissions for all vehicles based on engine size
predicted_co2 = reg_model.predict(X)

# Step 6: Categorization using pd.cut
# Define threshold values to categorize vehicles
thresholds = [0, 100, 200, float('inf')]  # Example thresholds for categories: Eco-Friendly, Moderate, Hazardous
labels = ['Eco-Friendly', 'Moderate', 'Hazardous']

# Create a new column 'Category' based on CO2 emission ranges
data['Category'] = pd.cut(predicted_co2, bins=thresholds, labels=labels)

# Step 7: Display the Resulting Dataset with the 'Category' Column
print(data[['Make', 'CO2 Emissions(g/km)', 'Category']])

