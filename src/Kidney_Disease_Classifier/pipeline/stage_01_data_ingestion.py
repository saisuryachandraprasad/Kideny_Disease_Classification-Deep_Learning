from src.Kidney_Disease_Classifier.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classifier.components.data_ingestion import DataIngestion
from src.Kidney_Disease_Classifier.utils.common import logger



STAGE_NAME = 'Data  Ingestion Stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.donwload_data()
        data_ingestion.unzip_file()



if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>>{STAGE_NAME} is completed<<<<<<<\n\nx==================x")

    except Exception as e:
        logger.info(e)
        raise e