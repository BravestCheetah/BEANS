from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers
from src.BEANS.io_api.rmem import restricted_memory
from src.BEANS.exit import exit
from src.BEANS.logger_global import logger
from src.BEANS.modlist import IO_MODULES

from src.BEANS.interpreter.op_api import handle_args

from threading import Thread
import os, importlib.util
from pathlib import Path
from platformdirs import user_data_dir


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index):  # type: ignore
        args = handle_args(args, ["num", "num", "num", "mem", "mem"])
        module_id = chr(args[0]) + chr(args[1]) + chr(args[2])
        memory_range = list(range(args[3], args[4] + 1))

        rmem = restricted_memory(mem[1], memory_range)
        biomods_dir = Path(user_data_dir("BEANS", "Cheetah")) / "BIOMods"  # BIOMods = BEANS IO Modules
        biomods_dir.mkdir(parents=True, exist_ok=True)

        module_path = biomods_dir / f"{module_id}.py"

        try:
            spec = importlib.util.spec_from_file_location(module_id, module_path)
            if spec is None or spec.loader is None:
                raise ImportError(f"Could not load module {module_id} at {module_path}")

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            mod = module.BIOMod(rmem, memory_range)  # expects BIOMod class inside the file
            IO_MODULES.append(mod) # type: ignore
            mod_command = mod.exec_module


            # Enable daemon so the sys.exit (found in the exit function imported)
            # will kill the threads as well
            mod_thread = Thread(target=mod_command, daemon=True)
            mod_thread.start()

        except Exception as e:
            logger.error(f"Failed To Load Module {module_id}: {e}") # type: ignore
            exit()

        return pc_index + 1
