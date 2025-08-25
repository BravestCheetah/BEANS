from usefullog.logger import Logger
from platformdirs import user_log_dir, user_data_dir



# A settings class containing all settings of the project, then we create an instance of the settings refrenced everywhere to get / set settings
# Initial settings = Default Settings

class _data:
    def __init__(self):
        
        self.logger = Logger(
            "BEANS",
            do_log_saving=True,
            log_save_folder=user_log_dir("BEANS", "Cheetah")
        )




data = _data()