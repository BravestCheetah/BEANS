class operation:
    def execute_operation(self, mem, args, pc_index):
        print(f"TEST got called with the args {str(args)}")
        return pc_index + 1