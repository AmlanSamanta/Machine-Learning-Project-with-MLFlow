from mlopsProject import logger
from mlopsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlopsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# logger.info("Welcome to the world of custom logging!")

# STAGE_NAME = "Data Ingestion Stage"
# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>>> {STAGE_NAME} started >>>>>>>>")
#         data_ingestion = DataIngestionTrainingPipeline()
#         data_ingestion.main()
#         logger.info(f">>>>>> {STAGE_NAME} completed >>>>>>")
#     except Exception as e:
#         logger.exception(e)
#         raise e

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started >>>>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
    

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e