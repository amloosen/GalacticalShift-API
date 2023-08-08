# These 2 imports are general for any api
from models.api_errors import ApiErrors
from models.base_object import BaseObject

# These are the custom models to import
from models.start_info import StartInfo
from models.slider_training import SliderTraining
from models.training_a import TrainingA
from models.training_b import TrainingB
from models.training_c import TrainingC
from models.main_task import MainTask
from models.task_params import TaskParams
from models.end_info import EndInfo
from models.data_backup import DataBackup
from models.quiz import Quiz

__all__ = (
    'ApiErrors',
    'BaseObject',
    'StartInfo',
)
