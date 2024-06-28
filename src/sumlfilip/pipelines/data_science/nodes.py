"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.6
"""
import logging
import random
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, accuracy_score, \
    precision_recall_curve, roc_curve, roc_auc_score


def split_data(data: pd.DataFrame):
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters_data_science.yml.
    Returns:
        Split data.
    """
    global label

    label = data.columns[1:]

    X = data.drop('HeartDisease', axis=1)  # 'HeartDisease' is the target column
    y = data['HeartDisease']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series):
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    # Create and train the Random Forest Classifier
    model_rfc = RandomForestClassifier(n_estimators=100, random_state=42)
    model_rfc.fit(X_train, y_train)

    # Create and train model based on logistic regression
    model_log= LogisticRegression(random_state=42, C=100)
    model_log.fit(X_train, y_train)

    # Create and train model based on SGD classifier
    model_sgd = SGDClassifier(alpha=0.01, random_state=42)
    model_sgd.fit(X_train, y_train)
    return model_rfc, model_log, model_sgd


def evaluate_model(model_rfc: RandomForestClassifier,model_log,model_sgd, X_test: pd.DataFrame, y_test: pd.Series):
    """Calculates and logs the coefficient of determination.

    Args:
        model_sgd:
        model_rfc:
        model_log:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """

    y_pred_rfc = model_rfc.predict(X_test)
    score = accuracy_score(y_test, y_pred_rfc)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient prediction of %.3f on test data.", score)

    y_pred_lod = model_log.predict(X_test)
    score = accuracy_score(y_test, y_pred_lod)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient prediction of %.3f on test data.", score)

    y_pred_sgd = model_sgd.predict(X_test)
    score = accuracy_score(y_test, y_pred_sgd)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient prediction of %.3f on test data.", score)


