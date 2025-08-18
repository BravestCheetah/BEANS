def _is_num(arg):
    return arg[0] == "int" or arg[0] == "bin"

def _get_args(args):
    return [arg[1] for arg in args]

def _check_args(args, expected_args):
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

def handle_args(args, expected_args):
    valid = _check_args(args, expected_args)

    import src.BEANS.logger_global as lg
    if not valid:
        lg.logger.error("Error: Args parsed was not valid") # type: ignore

    return _get_args(args)