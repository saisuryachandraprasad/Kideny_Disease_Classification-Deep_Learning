from src.Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Kidney_Disease_Classifier.utils.common import logger


STAGE_NAME = 'Data  Ingestion Stage'

try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>>{STAGE_NAME} is completed<<<<<<<\n\nx==================x")

except Exception as e:
        logger.info(e)
        raise e