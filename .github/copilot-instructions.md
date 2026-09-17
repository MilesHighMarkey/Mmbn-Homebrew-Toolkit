# Project Rules & Guidelines

- **Confidence Levels**: Explicitly list confidence levels for all findings using one of the following exact categories:
  - `Confirmed (Direct Observation)`
  - `Hypothesis (Under Test)`
  - `Unverified External Claim`
- **Verification Requirement**: Never assume external forum offsets or claims are fact without local debugger or disassembly verification.
- **Environment & Tooling**: All tools and automation scripts must be Windows-native Python or PowerShell scripts. Do not use Linux package managers (apt, pacman) or WSL-dependent commands.
- **Safe Execution**: Do not modify pristine/reference ROM files directly. Always copy ROMs to a working build folder before applying patches or modifications.
