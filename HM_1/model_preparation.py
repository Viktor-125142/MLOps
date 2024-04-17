import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib


def main():
    # Загрузка данных
    X_train = pd.read_csv('/Users/viktorilin/PycharmProjects/MLOps/HM_1/train/X_val_scaled.csv')
    y_train = pd.read_csv('/Users/viktorilin/PycharmProjects/MLOps/HM_1/train/y_val.csv')

    # Создание и обучение модели линейной регрессии
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Сохранение обученной модели
    joblib.dump(model, '/Users/viktorilin/PycharmProjects/MLOps/HM_1/model/linear_regression_model.pkl')

    # Опционально: Вычисление и вывод метрики модели
    y_pred = model.predict(X_train)
    mse = mean_squared_error(y_train, y_pred)
    print(f'Mean Squared Error: {mse}')


if __name__ == '__main__':
    main()
