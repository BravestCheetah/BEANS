from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore
        print(f"TEST got called!")
        return pc_index + 1