from src.ML_project import logger
from ML_project.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from ML_project.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e    


STAGE_NAME = " Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info((f">>>>> stage {STAGE_NAME} completed <<<<"))
except Exception as e:
    logger.exception(e)
    raise e    