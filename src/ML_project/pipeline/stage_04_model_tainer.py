from ML_project.config.configuration import ConfigurationManager
from ML_project.componenet.model_trainer import ModelTrainer
from ML_project import logger


STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>stage{STAGE_NAME}strated<<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>{STAGE_NAME} completed<<<<")

    except Exception as e:
        logger.exception(e)
        raise e    