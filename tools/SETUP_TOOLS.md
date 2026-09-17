# Tool Setup Guidance

This document outlines download sources, installation instructions, and recommended configurations for required Windows tools.

## 1. mGBA (Game Boy Advance Emulator & Debugger)
- **Purpose**: Running ROMs, debugging, scripting, memory inspection, and trace logging.
- **Download URL**: [https://mgba.io/downloads.html](https://mgba.io/downloads.html)
- **Recommended Package**: Windows x64 Installer or Portable ZIP.
- **Setup Steps**:
  1. Download and extract or install mGBA.
  2. If using portable mode, place executable in `tools/mgba/`.
  3. Recommended Debug settings: Enable the Scripting console and Symbol loading for GBA assembly debugging.

## 2. Ghidra (Software Reverse Engineering Suite)
- **Purpose**: Advanced static analysis, disassembly, and decompilation of ARM architecture GBA binaries.
- **Download URL**: [https://ghidra-sre.org/](https://ghidra-sre.org/)
- **Prerequisite**: Java Development Kit (JDK) 17 or higher (e.g., Eclipse Temurin JDK 17).
- **Setup Steps**:
  1. Install JDK 17 and ensure `JAVA_HOME` is configured.
  2. Download latest Ghidra release ZIP and extract to `tools/ghidra/`.
  3. Launch `ghidraRun.bat`.

## 3. HxD Hex Editor
- **Purpose**: Fast binary inspection, patching, and hex comparison of ROMs.
- **Download URL**: [https://mh-nexus.de/en/hxd/](https://mh-nexus.de/en/hxd/)
- **Recommended Package**: Setup or Portable Edition.
- **Setup Steps**:
  1. Download HxD and extract/install.
  2. Optional: Place portable executable in `tools/hxd/`.
