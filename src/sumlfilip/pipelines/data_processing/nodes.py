"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.6
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, accuracy_score, \
    precision_recall_curve, roc_curve, roc_auc_score
from sklearn.preprocessing import OneHotEncoder, RobustScaler, MinMaxScaler, StandardScaler
import joblib


def preprocess_hearth_data(data: pd.DataFrame) -> pd.DataFrame:
    data.describe().applymap(lambda x: f"{x:0.1f}")
    numeric_cols = ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']

    # Remove all records where sleep time is equal to 24 hours - it must be a measurement error
    data = data[data['SleepTime'] <24]

    # Replace all the outliers for variable 'SleepTime' with median
    median_sleep_time = data['SleepTime'].median()

    # Replace outliers (SleepTime > 16) with the median value
    data.loc[data['SleepTime'] > 16, 'SleepTime'] = median_sleep_time

    numeric_cols = data.select_dtypes('number').columns


    # Encode categorical columns
    def adjust_categorical_variable(var: str):
        if var == 'Yes':
            return 1
        else:
            return 0

    categorical_columns = data.dtypes == object
    categorical_columns = list(categorical_columns[categorical_columns].index)
    print(categorical_columns)

    # Apply adjust_categorical_variable() function where needed
    data[categorical_columns] = data[categorical_columns].applymap(adjust_categorical_variable)

    return data
