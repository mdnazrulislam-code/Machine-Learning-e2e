from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline




STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nx========================x")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Data Validation Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nx========================x")
    except Exception as e:
        logger.exception(e)
        raise e