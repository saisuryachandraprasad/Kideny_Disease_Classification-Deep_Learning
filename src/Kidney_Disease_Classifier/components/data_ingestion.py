import os
import gdown
import zipfile
from src.Kidney_Disease_Classifier import logger
from src.Kidney_Disease_Classifier.utils.common import get_size
from src.Kidney_Disease_Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    
    def donwload_data(self):
        """Fetch data from database"""

        try:
            dataset_url = self.config.source_url
            zipfile_dir = self.config.local_data_file

            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url}")

            file_url = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="

            gdown.download(prefix+file_url,zipfile_dir)

            logger.info(f"Downloaded data from {dataset_url}")

        except Exception as e:
            raise e
        
    def unzip_file(self):
        """unzip data after downloading """

        unzip_data_filepath = self.config.unzip_data
        os.makedirs(unzip_data_filepath,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_data_filepath)