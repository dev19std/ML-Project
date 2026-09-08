import os
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from ML_project.entity.congif_entity import ModelTrainerConfig
from ML_project import logger


class ModelEvaluation:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def eval_metrics(self, actual, predicted):
        mse = mean_squared_error(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)

        return mse, mae, r2

    def evaluate(self):

        test_data = pd.read_csv(self.config.test_data_path)

        test_x = test_data.drop(
            [self.config.target_column],
            axis=1
        )

        test_y = test_data[self.config.target_column]

        model_path = os.path.join(
            self.config.root_dir,
            self.config.model_name
        )

        model = joblib.load(model_path)

        predicted = model.predict(test_x)

        mse, mae, r2 = self.eval_metrics(
            test_y,
            predicted
        )

        # Log parameters and metrics to the active MLflow run
        mlflow.log_param(
            "alpha",
            self.config.alpha
        )

        mlflow.log_param(
            "l1_ratio",
            self.config.l1_ratio
        )

        mlflow.log_metric("mse", mse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        logger.info(f"Mean Squared Error: {mse}")
        logger.info(f"Mean Absolute Error: {mae}")
        logger.info(f"R2 Score: {r2}")