class register():

    def __init__(self, size):
        self.size = size
        self.val = 0
        self.max = 1 << self.size - 1

    def set(self, val):
        if val < 0 or val > self.max:
            raise ValueError(f"Value {val} does not fit in register with {self.size} bits")
        self.val = val
    
    def value(self):
        return format(self.val, f'0{self.size}b')