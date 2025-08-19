from src.BEANS.interpreter.memory.memory import memory

class restricted_memory:
    def __init__(self, memory: memory, access_adresses: list) -> None:
        self.mem = memory
        self.access_addresses = access_adresses

    def read(self, adress) -> int:

        if adress in self.access_addresses:
            return self.mem.memory.read(adress)