from src.ML_project import logger
from ML_project.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from ML_project.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from ML_project.pipeline.stage_3_data_transformatio import DataTransformationTrainingPipeline
from  ML_project.pipeline.stage_04_model_tainer import ModelTrainerTrainingPipeline

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

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    obj = DataTransformationTrainingPipeline()
    obj.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
        logger.info(f">>>>>>>>stage{STAGE_NAME}strated<<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>{STAGE_NAME} completed<<<<")

except Exception as e:
        logger.exception(e)
        raise e    
