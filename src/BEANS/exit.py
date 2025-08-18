import sys

def exit(msg: str = "Exiting the program..."):
    if msg:
        import src.BEANS.logger_global as lg
        lg.logger.critical(msg) # type: ignore
    sys.exit(1)