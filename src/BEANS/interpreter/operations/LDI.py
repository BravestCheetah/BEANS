from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore

        if len(args) != 2 or args[0][0] != "reg" or args[1][0] != "int":
            print("Wrong args lil bro")
        
        else:
            mem[0].write(int(args[0][1]), int(args[1][1])) # type: ignore

        return pc_index + 1