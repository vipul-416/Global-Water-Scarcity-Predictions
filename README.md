# Global Water Scarcity Prediction

## Project Overview

This project focuses on predicting global water scarcity levels using machine learning techniques.

The dataset contains global water consumption and environmental information from 2000 to 2025 across multiple countries.

The target variable is the Water Scarcity Level, which contains four categories:

- Low
- Moderate
- High
- Critical

## Dataset

The dataset contains 3,900 records covering 150 countries from 2000 to 2025.

### Features

- Country
- Year
- Total Water Consumption (Billion m3)
- Per Capita Water Use (L/Day)
- Agricultural Water Use (%)
- Industrial Water Use (%)
- Household Water Use (%)
- Rainfall Impact (mm)
- Groundwater Depletion Rate (%)

### Target

Water Scarcity Level

## Project Workflow

1. Data Loading
2. Data Understanding
3. Data Cleaning
4. Exploratory Data Analysis
5. Statistical Analysis
6. Feature Selection
7. Categorical Encoding
8. Train-Test Split
9. Handling Class Imbalance using SMOTE
10. Model Training
11. Stratified K-Fold Cross Validation
12. Hyperparameter Tuning using GridSearchCV
13. Model Evaluation
14. Feature Importance Analysis
15. Model Saving
16. Flask Deployment

## Machine Learning Models

The following classification models are used:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

## Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

## Class Imbalance

The target variable is imbalanced, with the Low scarcity category containing the majority of records.

SMOTE is applied to the training data to address class imbalance.

Stratified K-Fold Cross Validation is used during model validation to preserve class proportions across folds.

## Hyperparameter Tuning

GridSearchCV is used to tune the Random Forest classifier.

## Deployment

The trained machine learning model is saved as:

`water_scarcity_model.pkl`

A Flask application is used to provide a web interface for making predictions.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- XGBoost
- Flask
- Jupyter Notebook

## Project Structure
Global-Water-Scarcity-Prediction/
│
├── Global_Water_Scarcity_Prediction.ipynb
├── global_water_consumption_2000_2025.csv
├── app.py
├── water_scarcity_model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html

Author

Vipul

GitHub: https://github.com/vipul-416