from ML_project.config.configuration import ConfigurationManager
from ML_project.componenet.data_transformation import DataTransformation
from ML_project import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1].strip()

            if status == "True":
                config = ConfigurationManager()

                data_transformation_config = (
                    config.get_data_transformation_config()
                )

                data_transformation = DataTransformation(
                    config=data_transformation_config
                )

                data_transformation.Train_test_split()

            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
            logger.exception(e)
            raise e