# Ghidra Headless / Export Helper Stub
# Note: In Ghidra Python (Jython/PyGhidra), currentProgram and decompInterface are available when run inside Ghidra.
# This script is structured to be run via Ghidra headless analyzer or script manager.

import sys
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import TaskMonitor

def run():
    print("Exporting LoadMapHeader decompilation...")
    # Target address for LoadMapHeader
    addr_val = 0x08004514
    addr = currentProgram.getAddressFactory().getAddress(f"{addr_val:x}")
    
    func = currentProgram.getFunctionManager().getFunctionAt(addr)
    if not func:
        print(f"Function not found at {addr_val:x}")
        return

    decompiler = DecompInterface()
    decompiler.openProgram(currentProgram)
    res = decompiler.decompileFunction(func, 30, TaskMonitor.DUMMY)
    
    if not res.decompileCompleted():
        print("Decompilation failed.")
        return

    c_code = res.getDecompiledFunction().getC()
    
    # Write output to docs/map_load_function.c
    out_path = "docs/map_load_function.c"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"/* Decompiled from {addr_val:x} */\n")
        f.write(c_code)
    
    print(f"Successfully exported decompilation to {out_path}")

if __name__ == "__main__":
    run()
