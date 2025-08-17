from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.memory.registers import registers


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore

        if len(args) != 2 or args[0][0] != "reg" or args[1][0] != "reg" or args[2][0] != "reg":
            print("Wrong args lil bro")
        
        else:
            value = int(mem[0].read(args[0][0])) + int(mem[0].read(args[1][0]))
            mem[0].write(int(args[2][1]), value) # type: ignore

        return pc_index + 1