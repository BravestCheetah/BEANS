from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers

from src.BEANS.interpreter.op_api import handle_args


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore

        args = handle_args(args, ["num", "num", "num", "mem", "mem"])
        module_id = chr(args[0]) + chr(args[1]) + chr(args[2])
        memory_range = list(range(args[3], args[4] + 1))


        return pc_index + 1