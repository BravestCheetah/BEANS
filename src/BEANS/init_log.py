import src.BEANS.logger_global as lg
from platformdirs import user_data_dir

def init_logs():
    lg.logger.info("-------- BEANS ---------")
    lg.logger.info(" - Beans Is Initializing - ")
    lg.logger.info(f" - Beans IO Path: {user_data_dir("BEANS", "Cheetah")} - ")
    lg.logger.info("-------- BEANS ---------")