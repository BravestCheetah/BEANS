from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers

from src.BEANS.interpreter.op_api import check_args, get_val


class operation:

    @staticmethod
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore
        print(f"TEST got called! Argument 1 is num: {check_args(args, ["num"])} with value {get_val(args[0])}")
        return pc_index + 1