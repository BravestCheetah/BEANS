from sys import argv
import sys
import signal
import os
from pathlib import Path

from src.BEANS.BEANS_GUI.gui import BEANSGui
from src.BEANS.interpreter.interpreter import interpret_line
from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers

from usefullog.logger import Logger
from platformdirs import user_log_dir

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication


class BEANSExecutor:
    def __init__(self, path, gui, logger, mem, regs):
        self.code_path = path
        self.gui = gui
        self.logger = logger
        self.mem = mem
        self.regs = regs

        with open(self.code_path, "r") as f:
            self.lines = f.readlines()

        self.index = 0

    def step(self):
        if self.index >= len(self.lines):
            return  # finished program

        line = self.lines[self.index].strip()
        if not line or line.startswith("//"):
            self.index += 1
            return

        # run one line
        self.index = interpret_line(line, self.regs, self.mem, self.index)

        # update GUI labels here
        self.gui.label_last_op.setText(f"Last Operation: {line}")
        self.gui.label_last_op_line.setText(
            f"Line: {self.index} / {len(self.lines)}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Ctrl+C works

    # --- setup logging + memory ---
    os.makedirs(user_log_dir("BEANS", "Cheetah"), exist_ok=True)
    logger = Logger(
        "BEANS",
        do_log_saving=True,
        log_save_folder=user_log_dir("BEANS", "Cheetah")
    )

    mem = memory(32, 8)
    regs = registers(8, 8)

    # --- build executor + gui ---
    gui = BEANSGui(argv[1], logger)
    executor = BEANSExecutor(argv[1], gui, logger, mem, regs)

    gui.show()

    timer = QTimer()
    timer.timeout.connect(executor.step)
    timer.start(0)  # run as fast as possible

    sys.exit(app.exec())
