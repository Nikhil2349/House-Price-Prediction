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
- [Directory Structure](#directory-structure)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The objective of this project is to build a predictive model for house prices in Bengaluru. We use various regression algorithms to predict the prices and evaluate their performance. Additionally, a Flask web application is developed to provide an interactive interface for users to input house features and get price predictions.

## Dataset

The dataset used in this project is `Bengaluru_House_Data.csv`. It contains the following columns:

- `area_type`: Type of the area (e.g., Super built-up Area, Built-up Area, Plot Area, Carpet Area)
- `availability`: When the property is available (e.g., Ready To Move, Immediate Possession)
- `location`: Location of the property
- `size`: Number of bedrooms (BHK)
- `society`: Name of the society
- `total_sqft`: Total area in square feet
- `bath`: Number of bathrooms
- `balcony`: Number of balconies
- `price`: Price of the property in lakhs

## Preprocessing and EDA

The data preprocessing and Exploratory Data Analysis (EDA) steps include:

- **Handling Missing Values**: Filling missing values with appropriate measures (e.g., median, mode).
- **Converting Categorical Data to Numerical Data**: Using one-hot encoding for categorical features.
- **Removing Outliers**: Identifying and removing outliers based on domain knowledge and statistical methods.
- **Feature Engineering**: Creating new features such as `price_per_sqft` for better model performance.
- **Data Visualization**: Using various plots (e.g., histograms, bar plots, scatter plots) to understand the distribution and relationships of features.

## Model Training

We train the following models on the preprocessed data:

1. **Linear Regression**
2. **Lasso Regression**
3. **Ridge Regression**
4. **Random Forest Regression**

The models are evaluated using a pipeline that includes preprocessing steps like scaling and one-hot encoding.

## Evaluation

The performance of the models is evaluated using the following metrics:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R-squared (R2)**

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
