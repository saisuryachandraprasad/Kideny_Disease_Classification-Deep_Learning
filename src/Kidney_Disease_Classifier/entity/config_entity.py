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