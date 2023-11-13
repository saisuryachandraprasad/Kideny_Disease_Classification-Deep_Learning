from src.Kidney_Disease_Classifier.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classifier.components.model_training import Training
from src.Kidney_Disease_Classifier.utils.common import logger


STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass



    def main(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer()
        training = Training(config= trainer_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>{STAGE_NAME} is started <<<<<<<<<<<")

        model_training = ModelTrainingPipeline()
        model_training.main()

        logger.info(f">>>>>>>>>>{STAGE_NAME} is completed <<<<<<<<<</n/n X===================X")

    except Exception as e:
        logger.info(e)
        raise e
