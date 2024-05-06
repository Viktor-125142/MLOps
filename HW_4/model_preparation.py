import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error as mse
import joblib
import hydra
from omegaconf import DictConfig
import logging

log = logging.getLogger(__name__)

from pipeline import preprocessors_all
from metric.metric_mse_r2 import calculate_metric

@hydra.main(version_base=None, config_path='config', config_name='config')
def model_preparation(cfg: DictConfig):
    X_train = pd.read_csv("test/X_train.csv")
    y_train = pd.read_csv("test/y_train.csv").squeeze()

    pipe_all = Pipeline([
        ('preprocessors', preprocessors_all),
        ('model', DecisionTreeRegressor(
            max_leaf_nodes=cfg.model.params.max_leaf_nodes,
            min_samples_split=cfg.model.params.min_samples_split,
            criterion=cfg.model.params.criterion
        ))
    ])

    pipe_all.fit(X_train, y_train)

    joblib.dump(pipe_all, 'model/DecisionTreeRegressor_model.pkl')

    log.info(f"r2 на тренировочной выборке: {calculate_metric(pipe_all, X_train, y_train):.4f}")
    log.info(f"mse на тренировочной выборке: {calculate_metric(pipe_all, X_train, y_train, mse):.4f}")


if __name__ == "__main__":
    model_preparation()
