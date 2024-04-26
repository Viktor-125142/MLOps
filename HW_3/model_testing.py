from sklearn.metrics import mean_squared_error as mse
import pandas as pd
import joblib

from metric.metric_mse_r2 import calculate_metric


def predict():
    X_train = pd.read_csv('train/X_val.csv')
    y_train = pd.read_csv('train/y_val.csv')

    model = joblib.load('model/DecisionTreeRegressor_model.pkl')

    predict_new_data = model.predict(X_train)

    print(f"r2 на валидационной выборке: {calculate_metric(model, X_train, y_train):.4f}")
    print(f"mse на валидационной выборке: {calculate_metric(model, X_train, y_train, mse):.4f}")


