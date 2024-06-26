from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline



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
    

STAGE_NAME = "Data Transformation Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nx========================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Trainer "
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nx========================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Evaluation "
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<\n\nx========================x")
    except Exception as e:
        logger.exception(e)
        raise e