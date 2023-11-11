from src.Kidney_Disease_Classifier.constants import *
from src.Kidney_Disease_Classifier.utils.common import read_yaml, create_directories
from src.Kidney_Disease_Classifier.entity.config_entity import (DataIngestionConfig,
                                                                PrepareBaseModelConfig)



class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url= config.source_url,
            local_data_file= config.local_data_file,
            unzip_data=config.unzip_data
        )

        return data_ingestion_config
    


    def get_prepare_base_model(self):
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_model_path = Path(config.updated_model_path),
            params_IMAGE_SIZE = self.params.IMAGE_SIZE,
            params_WEIGHTS = self.params.WEIGHTS,
            params_INCLUDE_TOP = self.params.INCLUDE_TOP,
            params_LEARNING_RATE = self.params.LEARNING_RATE,
            params_CLASSES = self.params.CLASSES

        )
        return prepare_base_model_config
