from src.Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Kidney_Disease_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.Kidney_Disease_Classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
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




STAGE_NAME = "Prepare Base Model stage"

try:
             
        logger.info(f">>>>>>>{STAGE_NAME} is started<<<<<<<<< ")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>{STAGE_NAME} is completed <<<<<<<<\n\n x===============x")

except Exception as e:
        logger.info(e)
        raise e


STAGE_NAME = "Model Training"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>{STAGE_NAME} is started <<<<<<<<<<<")

        model_training = ModelTrainingPipeline()
        model_training.main()

        logger.info(f">>>>>>>>>>{STAGE_NAME} is completed <<<<<<<<<</n/n X===================X")

    except Exception as e:
        logger.info(e)
        raise e