import src.BEANS.logger_global as lg
from platformdirs import user_data_dir

def init_logs():
    lg.logger.info("-------- BEANS ---------") # type: ignore
    lg.logger.info(" - Beans Is Initializing - ") # type: ignore
    lg.logger.info(f" - Beans IO Path: {user_data_dir("BEANS", "Cheetah")} - ") # type: ignore
    lg.logger.info("-------- BEANS ---------") # type: ignore