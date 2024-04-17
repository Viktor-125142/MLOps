import numpy as np
import pandas as pd


# Генирируем данные
Monday = np.random.uniform(low=0, high=40, size=1000)
Tuesday = np.random.uniform(low=0, high=40, size=1000)
Wednesday = np.random.uniform(low=0, high=40, size=1000)
Thursday = np.random.uniform(low=0, high=40, size=1000)
Friday = np.random.uniform(low=0, high=40, size=1000)
Saturday = np.random.uniform(low=0, high=40, size=1000)
Sunday = np.random.uniform(low=0, high=40, size=1000)


# Генирируем шум
noise = np.random.normal(loc=0, scale=1, size=Monday.shape)


# Добавляем шум к нашим данным
Monday = Monday + noise
Tuesday = Tuesday + noise
Wednesday = Wednesday + noise
Thursday = Thursday + noise
Friday = Friday + noise
Saturday = Saturday + noise
Sunday = Sunday + noise

# Создание DataFrame
temperatures = pd.DataFrame({
    'Monday': Monday,
    'Tuesday': Tuesday,
    'Wednesday': Wednesday,
    'Thursday': Thursday,
    'Friday': Friday,
    'Saturday': Saturday,
    'Sunday': Sunday
})


if __name__ == '__main__':
    temperatures.to_csv('/Users/viktorilin/PycharmProjects/MLOps/HM_1/data/dataweekly_temperatures.csv', index=False)