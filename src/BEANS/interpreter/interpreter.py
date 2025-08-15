from src.BEANS.interpreter.memory.registers import registers
from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.operation_handler import execute_operation

def interpret(file_path: str):
    regs = registers(8, 16)
    mem = memory(32, 8)

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line == '' or line[0] == '#':
                continue
            code = line.split(' ')
            execute_operation(code[0], (regs, mem), code[1:])