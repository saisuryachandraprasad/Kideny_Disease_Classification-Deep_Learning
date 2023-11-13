from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_data: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_model_path: Path
    params_IMAGE_SIZE: list
    params_WEIGHTS: str
    params_INCLUDE_TOP: bool
    params_LEARNING_RATE: float
    params_CLASSES: int


@dataclass (frozen= True)
class TrainingConfig:
    root_dir :Path
    trained_model_path: Path
    updated_model_path: Path
    training_data: Path
    params_epoch: int
    params_batch_size: int
    params_is_augamentation: bool
    params_image_size:list


@dataclass(frozen= True)
class EvaluationConfig:
    path_of_model : Path
    training_data :Path
    all_params : dict
    params_batch_size :int
    params_image_size :list
    mlflow_uri : str