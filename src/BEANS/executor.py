from sys import argv

from src.BEANS.BEANS_GUI.gui import BEANSGui
from src.BEANS.interpreter.interpreter import interpret_line
from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers

from usefullog.logger import Logger
from pathlib import Path
from platformdirs import user_log_dir
import os

from PyQt6.QtWidgets import QApplication
from sys import argv

class BEANSExecturor():
    def __init__(self, path):

        self.app = QApplication(argv)

        self.code_path = path
        os.makedirs(user_log_dir("BEANS", "Cheetah"), exist_ok=True)
        self.logger = Logger("BEANS", do_log_saving=True, log_save_folder=user_log_dir("BEANS", "Cheetah"))

        self.logger.info("BEANS Executor Initialization Process is starting...")

        # TODO: Add these params as options for the user using flags in the future.
        self.mem = memory(32, 8)
        self.regs = registers(8, 8)

        self.gui = BEANSGui(self.code_path, self.logger)
        self.gui.show()

        self.logger.info("BEANS Executor Initialization Process Has Finished, starting interpretation process")

        with open(self.code_path, "r") as f:
            lines = f.readlines()

            index = 0
            while index <= len(lines) - 1:
                line = lines[index].strip()

                if line == '' or line[0:1] == '//':
                    index += 1
                    continue

                index = interpret_line(line, self.regs, self.mem, index)


executor = BEANSExecturor(argv[1])
