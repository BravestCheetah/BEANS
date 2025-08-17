class operation:
    def execute_operation(mem, args, pc_index): # type: ignore

        if len(args) != 2 or args[0][0] != "reg" or args[1][0] != "int":
            print("Wrong args lil bro")
        
        else:
            mem[0].write(int(args[0][1]), int(args[1][1])) # type: ignore

        return pc_index + 1