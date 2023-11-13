from src.Kidney_Disease_Classifier.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classifier.components.model_evaluation_with_mlflow import Evaluation
from src.Kidney_Disease_Classifier.utils.common import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ =="__main__":
    try:

        logger.info(f">>>>>>>>>>{STAGE_NAME} is started ")

        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()

        logger.info(f">>>>>>>>>{STAGE_NAME} is completed <<<<<<<<<< /n/n X==============X")

    except Exception as e:
        logger.info(e)
        raise e