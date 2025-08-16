from src.BEANS.interpreter.memory.registers import registers
from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.operation_handler import execute_operation

def interpret_line(line: str, regs: registers, mem: memory, pc_index: int):
    code = line.split(' ')
    return execute_operation(code[0], (regs, mem), code[1:], pc_index)