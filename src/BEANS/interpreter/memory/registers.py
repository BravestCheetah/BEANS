class register():

    def __init__(self, size):
        self.size = size
        self.val = 0
        self.max = (1 << self.size) - 1

    def set(self, val):
        self.val = val & self.max
    
    def value(self):
        return self.val


class registers():

    def __init__(self, reg_size, reg_num):

        self.regs: list[register] = []
        for i in range(reg_num):
            self.regs.append(register(reg_size))
    
    def read(self, reg: int) -> int:
        return self.regs[reg].value()
    
    def write(self, reg: int, val):
        self.regs[reg].set(val)