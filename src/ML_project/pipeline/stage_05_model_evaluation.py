from ML_project.config.configuration import ConfigurationManager
from ML_project.componenet.model_evaluation import ModelEvaluation
from ML_project import logger
import mlflow
import dagshub


STAGE_NAME = "Model Evaluation stage"


class ModelEvaluationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()

            model_evaluation_config = config.get_model_trainer_config()

            model_evaluation = ModelEvaluation(
                config=model_evaluation_config
            )

            dagshub.init(
                repo_owner="dev19std",
                repo_name="ML-Project",
                mlflow=True
            )

            with mlflow.start_run():
                model_evaluation.evaluate()

        except Exception as e:
            logger.exception(e)
            raise e