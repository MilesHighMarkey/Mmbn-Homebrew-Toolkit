# Map 0 Header & Layout Analysis

- **ROM Header Offset**: `0x00511580`
- **Confidence Level**: `Confirmed (Direct Observation)`

## Raw Header Fields (32 bytes / 8 dwords)
| Index | Raw Value (Hex) | Raw Value (Decimal) | Potential Field Description |
| :---: | :---: | :--- | :--- |
| 0 | `0x000001A0` | 416 | Width / Tilemap Pointer 1 |
| 1 | `0xCFF97C00` | 3489233920 | Height / Tilemap Pointer 2 |
| 2 | `0xBFD4C7D6` | 3218393046 | Layout / Attributes Pointer |
| 3 | `0xB3AFB7D1` | 3014637521 | Palette / Tileset Pointer |
| 4 | `0x9F67A78B` | 2674370443 | Event Script Pointer |
| 5 | `0x96409322` | 2520814370 | Layer Data / Flags |
| 6 | `0xD6F08023` | 3606085667 | Properties / Music ID |
| 7 | `0xC699D2EE` | 3331969774 | Border / Collision Pointer |

## Raw Byte Dump
```hex
00511580: A0 01 00 00 00 7C F9 CF D6 C7 D4 BF D1 B7 AF B3   .....|..........
00511590: 8B A7 67 9F 22 93 40 96 23 80 F0 D6 EE D2 99 C6   ..g.".@.#.......
```
