import os
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

from ML_project.entity.congif_entity import ModelTrainerConfig
from ML_project import logger



class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        model = ElasticNet(
        alpha=self.config.alpha,
        l1_ratio=self.config.l1_ratio,
        random_state=42 )

        model.fit(train_x, train_y)
        predictions = model.predict(test_x)
        mse = mean_squared_error(test_y, predictions)
        mae = mean_absolute_error(test_y, predictions)
        r2 = r2_score(test_y, predictions)


        logger.info(f"Mean Squared Error: {mse}")
        logger.info(f"Mean Absolute Error: {mae}")
        logger.info(f"R2 Score: {r2}")
        

        model_path = os.path.join(
                self.config.root_dir,
                self.config.model_name
            )
        
        joblib.dump(model, model_path)
        
        logger.info(f"Model saved at: {model_path}")    

    