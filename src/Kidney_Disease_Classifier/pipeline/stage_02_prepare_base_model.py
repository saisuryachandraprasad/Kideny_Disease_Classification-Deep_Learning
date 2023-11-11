from src.Kidney_Disease_Classifier.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classifier.components.prepare_base_model import PrepareBaseModel
from src.Kidney_Disease_Classifier.utils.common import logger



STAGE_NAME = "Prepare Base Model stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass



    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config= config.get_prepare_base_model()
        prepare_base_model = PrepareBaseModel(config= prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == "__main__":

    try:
             
        logger.info(f">>>>>>>{STAGE_NAME} is started<<<<<<<<< ")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>{STAGE_NAME} is completed <<<<<<<<\n\n x===============x")

    except Exception as e:
        logger.info(e)
        raise e
