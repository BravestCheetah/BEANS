from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.memory.registers import registers


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore
        return float("inf")