#!/usr/bin/env python3
"""
tools/build_rom.py
Mega Man Battle Network 1 (US) Master Build Script & End-to-End Release Gate.
Chains scene compilation, event encoding, SCB compilation, map allocation,
and playthrough validation into a single automated pipeline.
"""
from pathlib import Path
import subprocess
import sys

ROM_PATH = Path("roms/BN1_US.gba")

def run_step(script_name: str):
    script_path = Path(f"tools/{script_name}")
    print(f"\n[BUILD PIPELINE] Running step: {script_name}...")
    if not script_path.exists():
        print(f"[ERROR] Required tool not found: {script_path}")
        return False
    
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
        
    if result.returncode != 0:
        print(f"[ERROR] Step {script_name} failed with exit code {result.returncode}")
        return False
    print(f"[SUCCESS] Step {script_name} completed successfully.")
    return True

def main():
    print("=== Mega Man Battle Network 1 (US) Master Build Pipeline ===")
    if not ROM_PATH.exists():
        print(f"[ERROR] Clean reference ROM not found at {ROM_PATH}")
        sys.exit(1)

    steps = [
        "scene_compiler.py",
        "event_encoder.py",
        "scb_compiler.py",
        "map_allocator.py",
        "playthrough_validator.py"
    ]

    for step in steps:
        if not run_step(step):
            print("\n[BUILD FAILURE] Master build pipeline aborted due to step failure.")
            sys.exit(1)

    print("\n" + "="*60)
    print("[SUCCESS] MASTER BUILD PIPELINE COMPLETED SUCCESSFULLY!")
    print("All modules (Scene Compiler, Event Encoder, SCB Compiler, Map Allocator,")
    print("and Playthrough Validator) executed error-free. Custom modded ROM is ready.")
    print("="*60)

if __name__ == "__main__":
    main()
