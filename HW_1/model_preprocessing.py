import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def main():
    # Загрузка данных
    df = pd.read_csv("/Users/viktorilin/PycharmProjects/MLOps/HW_1/data/dataweekly_temperatures.csv")

    # Разделение данных на признаки и целевую переменную
    X, y = df.drop(columns=['Sunday']), df['Sunday']

    # Разделение данных на обучающую и валидационную выборки
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

    # Инициализация и обучение стандартизатора
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    # Сохранение обработанных данных
    pd.DataFrame(X_train_scaled, index=X_train.index, columns=X_train.columns).to_csv('/Users/viktorilin/PycharmProjects/MLOps/HW_1/test/X_train_scaled.csv', index=False)
    pd.DataFrame(X_val_scaled, index=X_val.index, columns=X_val.columns).to_csv('/Users/viktorilin/PycharmProjects/MLOps/HW_1/train//X_val_scaled.csv', index=False)
    y_train.to_csv('/Users/viktorilin/PycharmProjects/MLOps/HW_1/test/y_train.csv', index=False)
    y_val.to_csv('/Users/viktorilin/PycharmProjects/MLOps/HW_1/train/y_val.csv', index=False)


if __name__ == '__main__':
    main()
