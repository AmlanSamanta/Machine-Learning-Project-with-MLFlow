from mlopsProject import logger
from mlopsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# logger.info("Welcome to the world of custom logging!")

STAGE_NAME = "Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started >>>>>>>>")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> {STAGE_NAME} completed >>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e