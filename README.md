# House Price Prediction Model

This project involves building a machine learning model to predict house prices in Bengaluru. The model uses various features such as location, area type, number of bedrooms (BHK), number of bathrooms, and total square feet to predict the house price. This project also includes a Flask web application for user interaction.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Preprocessing and EDA](#preprocessing-and-eda)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The objective of this project is to build a predictive model for house prices in Bengaluru. We use various regression algorithms to predict the prices and evaluate their performance.

## Dataset

The dataset used in this project is `Bengaluru_House_Data.csv`. It contains the following columns:

- `area_type`
- `availability`
- `location`
- `size`
- `society`
- `total_sqft`
- `bath`
- `balcony`
- `price`

## Preprocessing and EDA

The data preprocessing and Exploratory Data Analysis (EDA) steps include:

- Handling missing values
- Converting categorical data to numerical data
- Removing outliers
- Feature engineering (e.g., creating `price_per_sqft`)
- Data visualization to understand the distribution and relationships of features

## Model Training

We train the following models on the preprocessed data:

1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. Random Forest Regression

## Evaluation

The performance of the models is evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R2)

### Model Performance

| Model                   | R2 Score | MAE       |
|-------------------------|----------|-----------|
| Linear Regression       | 0.856    | 19.13     |
| Lasso Regression        | 0.710    | 24.36     |
| Ridge Regression        | 0.856    | 18.38     |
| Random Forest Regression| 0.838    | 16.55     |

## Web Application

A simple Flask web application is developed to interact with the model. The app allows users to input the features and get the predicted price.

### Flask App Structure

- **`app.py`**: The main Flask application file.
- **`templates/index.html`**: The HTML template for the web interface.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
