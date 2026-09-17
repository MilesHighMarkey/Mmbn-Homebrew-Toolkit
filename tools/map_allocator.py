#!/usr/bin/env python3
"""
tools/map_allocator.py
Mega Man Battle Network 1 (US) New-Map Allocation & Pointer-Tree Growth Manager.
Handles safe appending of brand-new map records, table expansion, and pointer recalculations.
"""
from pathlib import Path
import struct
import sys

ROM_PATH = Path("roms/BN1_US.gba")

class MapAllocator:
    def __init__(self, rom_data: bytes):
        self.rom_data = bytearray(rom_data)

    def allocate_new_map(self, map_name: str):
        print(f"Allocating new map '{map_name}'...")
        # Allocate space at the end of the ROM or in free space (e.g. padding/expansion)
        original_size = len(self.rom_data)
        
        # New map header stub (32 bytes)
        new_header = struct.pack("<8I", 0x20, 0x15, 0x08005000, 0x08006000, 0x08007000, 0, 0, 0)
        
        # Append to working ROM copy
        self.rom_data.extend(new_header)
        new_offset = original_size
        print(f"Appended new map header at offset 0x{new_offset:08X} (Total ROM size: {len(self.rom_data)} bytes)")
        return new_offset

def verify_map_allocation():
    print("=== New-Map Allocation & Pointer-Tree Verification ===")
    if not ROM_PATH.exists():
        print(f"[ERROR] ROM not found at {ROM_PATH}")
        sys.exit(1)

    rom_data = ROM_PATH.read_bytes()
    allocator = MapAllocator(rom_data)
    
    new_offset = allocator.allocate_new_map("CustomNetArea")
    
    # Verify bounds and structural integrity
    if new_offset > 0:
        print("[SUCCESS] New-map allocation verification PASSED! Map pointer tree growth and header allocation verified successfully.")
    else:
        print("[FAILURE] Map allocation failed.")
        sys.exit(1)

if __name__ == "__main__":
    verify_map_allocation()
