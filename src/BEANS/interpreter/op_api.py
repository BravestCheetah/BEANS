def _is_num(arg):
    return arg[0] == "int" or arg[0] == "bin"

def get_val(arg):
    return arg[1]

def check_args(args, expected_args):
    if len(args) != len(expected_args):
        return False
    
    for i in range(len(args)):
        if expected_args[i] == "num":
            if not _is_num(args[i]):
                return False
        else:
            if args[i][0] != expected_args[i]:
                return False
    
    return True