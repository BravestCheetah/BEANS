from src.BEANS.interpreter.memory.registers import registers
from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.operation_handler import execute_operation

def parse_args(args: list[str]) -> list:
    
    parsed = []

    for arg in args:
        if arg.startswith("r"):
            parsed.append(("reg", arg[1:]))
        
        elif arg.startswith("m"):
            parsed.append(("mem", arg[1:]))

        elif arg.startswith("io"):
            parsed.append(("io", arg[2:]))

        elif arg.startswith("i"):
            parsed.append(("int", arg[1:]))
        
    return parsed

def interpret_line(line: str, regs: registers, mem: memory, pc_index: int):
    code = line.split(' ')
    return execute_operation(code[0], (regs, mem), parse_args(code[1:]), pc_index)