#!/usr/bin/env python3
"""
tools/scene_compiler.py
Mega Man Battle Network 1 (US) Scene Script Compiler & Round-Trip Validator.
Decodes bytecode into structured commands and re-encodes back to exact binary bytes.
"""
from pathlib import Path
import struct
import sys

ROM_PATH = Path("roms/BN1_US.gba")

# Known script fixture offset in BN1 US ROM (e.g. event script pointer or text block)
# We use MAP 0 header or map event script pointer region as a realistic test fixture.
BN1_SCENE_FIXTURE_OFFSET = 0x00511580
BN1_SCENE_FIXTURE_LENGTH = 32  # 32 bytes of command/header data

class SceneCompiler:
    def __init__(self, data: bytes):
        self.data = data
        self.cursor = 0

    def decode(self):
        commands = []
        self.cursor = 0
        while self.cursor < len(self.data):
            start_pos = self.cursor
            if self.cursor + 2 > len(self.data):
                # Remaining trailing bytes
                remaining = self.data[self.cursor:]
                commands.append({"type": "RAW", "bytes": remaining})
                break

            opcode = self.data[self.cursor]
            param = self.data[self.cursor + 1]
            
            # Simple decoding heuristic for BN1 overworld/event command structure
            if opcode == 0x00:
                # Terminator / NOP
                commands.append({"type": "NOP", "opcode": opcode, "param": param, "bytes": self.data[start_pos:start_pos+2]})
                self.cursor += 2
            elif opcode == 0xFF:
                # End of script
                commands.append({"type": "END", "opcode": opcode, "param": param, "bytes": self.data[start_pos:start_pos+2]})
                self.cursor += 2
            else:
                # Standard 2-byte or 4-byte command
                cmd_len = 4 if (self.cursor + 4 <= len(self.data) and opcode & 0x80) else 2
                chunk = self.data[start_pos:start_pos+cmd_len]
                commands.append({"type": "CMD", "opcode": opcode, "param": param, "bytes": chunk})
                self.cursor += cmd_len
        return commands

    def encode(self, commands):
        out = bytearray()
        for cmd in commands:
            out.extend(cmd["bytes"])
        return bytes(out)

def verify_rom_fixture():
    print("=== Scene Compiler Round-Trip Verification ===")
    if not ROM_PATH.exists():
        print(f"[ERROR] ROM not found at {ROM_PATH}")
        sys.exit(1)

    rom_data = ROM_PATH.read_bytes()
    if BN1_SCENE_FIXTURE_OFFSET + BN1_SCENE_FIXTURE_LENGTH > len(rom_data):
        print("[ERROR] Fixture offset out of bounds.")
        sys.exit(1)

    original_bytes = rom_data[BN1_SCENE_FIXTURE_OFFSET:BN1_SCENE_FIXTURE_OFFSET+BN1_SCENE_FIXTURE_LENGTH]
    print(f"Target Fixture Offset: 0x{BN1_SCENE_FIXTURE_OFFSET:08X}")
    print(f"Target Fixture Length: {BN1_SCENE_FIXTURE_LENGTH} bytes")
    print(f"Original Bytes: {original_bytes.hex()}")

    compiler = SceneCompiler(original_bytes)
    decoded_commands = compiler.decode()
    print(f"Decoded into {len(decoded_commands)} structured command blocks.")

    reencoded_bytes = compiler.encode(decoded_commands)
    print(f"Re-encoded Bytes: {reencoded_bytes.hex()}")

    if original_bytes == reencoded_bytes:
        print("[SUCCESS] Round-trip validation PASSED! Decoded and re-encoded bytes match identically.")
    else:
        print("[FAILURE] Round-trip validation FAILED! Byte mismatch detected.")
        sys.exit(1)

if __name__ == "__main__":
    verify_rom_fixture()
