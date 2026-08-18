from ML_project.config.configuration import ConfigurationManager
from ML_project.componenet.data_ingestion import DataIngestion
from ML_project import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(sefl):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file() 

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage{STAGE_NAME} started<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<\n\n x==========x")
    except Exception as e:
        logger.exception(e)
        raise e    
