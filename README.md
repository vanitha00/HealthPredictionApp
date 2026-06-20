# Health Prediction Application

## Overview

The Health Prediction Application is a web-based application developed using Streamlit, SQLite, and Scikit-learn. It allows users to manage patient records and predict health risks based on medical parameters such as Glucose, Haemoglobin, and Cholesterol levels.

## Features

* Add Patient Records
* View Patient Records
* Update Patient Records
* Delete Patient Records
* Health Risk Prediction using Machine Learning
* Email Validation
* Date Validation
* SQLite Database Storage
* User-Friendly Streamlit Interface

## Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
* Scikit-learn
* Decision Tree Classifier

## Project Structure

HealthPredictionApp/

* app.py
* database.py
* prediction.py
* health_data.csv
* patients.db
* requirements.txt
* README.md

## Machine Learning Model

The application uses a Decision Tree Classifier from Scikit-learn. The model is trained using sample health data containing:

* Glucose
* Haemoglobin
* Cholesterol
* Risk Label

The trained model predicts whether a patient is at health risk or has normal health indicators.

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the application:

python -m streamlit run app.py

3. Open the local Streamlit URL displayed in the terminal.

## Author

Kotla Vanitha
