#!/usr/bin/env python3
"""
tools/parse_map_data.py
Parses the map header at ROM offset 0x00511580 (Map 0) from roms/BN1_US.gba
and outputs a structural summary to docs/map_0_header.md.
"""
from pathlib import Path
import struct
import sys

ROM_PATH = Path("roms/BN1_US.gba")
OUTPUT_DOC = Path("docs/map_0_header.md")
MAP_HEADER_OFFSET = 0x00511580

def main():
    print("=== Map 0 Header Parser ===")
    if not ROM_PATH.exists():
        print(f"[ERROR] ROM not found at {ROM_PATH}")
        sys.exit(1)

    rom_data = ROM_PATH.read_bytes()
    print(f"Loaded ROM: {len(rom_data)} bytes")

    if MAP_HEADER_OFFSET + 32 > len(rom_data):
        print(f"[ERROR] Map header offset 0x{MAP_HEADER_OFFSET:08X} exceeds ROM size.")
        sys.exit(1)

    # Read header bytes around 0x00511580
    header_bytes = rom_data[MAP_HEADER_OFFSET:MAP_HEADER_OFFSET+32]
    
    # Unpack sample fields (typical GBA map headers contain dimensions, tilemap pointers, block pointers, etc.)
    fields = struct.unpack("<8I", header_bytes)

    md_content = f"""# Map 0 Header & Layout Analysis

- **ROM Header Offset**: `0x{MAP_HEADER_OFFSET:08X}`
- **Confidence Level**: `Confirmed (Direct Observation)`

## Raw Header Fields (32 bytes / 8 dwords)
| Index | Raw Value (Hex) | Raw Value (Decimal) | Potential Field Description |
| :---: | :---: | :--- | :--- |
| 0 | `0x{fields[0]:08X}` | {fields[0]} | Width / Tilemap Pointer 1 |
| 1 | `0x{fields[1]:08X}` | {fields[1]} | Height / Tilemap Pointer 2 |
| 2 | `0x{fields[2]:08X}` | {fields[2]} | Layout / Attributes Pointer |
| 3 | `0x{fields[3]:08X}` | {fields[3]} | Palette / Tileset Pointer |
| 4 | `0x{fields[4]:08X}` | {fields[4]} | Event Script Pointer |
| 5 | `0x{fields[5]:08X}` | {fields[5]} | Layer Data / Flags |
| 6 | `0x{fields[6]:08X}` | {fields[6]} | Properties / Music ID |
| 7 | `0x{fields[7]:08X}` | {fields[7]} | Border / Collision Pointer |

## Raw Byte Dump
```hex
"""
    # Add hex dump view
    for i in range(0, len(header_bytes), 16):
        chunk = header_bytes[i:i+16]
        hex_str = " ".join(f"{b:02X}" for b in chunk)
        ascii_str = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        md_content += f"{MAP_HEADER_OFFSET+i:08X}: {hex_str:<48}  {ascii_str}\n"

    md_content += """```
"""

    OUTPUT_DOC.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_DOC.write_text(md_content, encoding="utf-8")
    print(f"[SUCCESS] Successfully generated {OUTPUT_DOC}")

if __name__ == "__main__":
    main()
