# Encode/Decode String Program

## Overview
This Python program provides two functions:
1. `encode(strs)`: Converts a list of strings into a single encoded string.
2. `decode(encoded_str)`: Decodes the encoded string back into the original list of strings.

This method ensures that strings containing special characters or numbers can be accurately encoded and decoded.

## How It Works
- **Encoding**: Each string is prefixed with its length, followed by a `#` delimiter.
- **Decoding**: The function reads the length prefix, extracts the string, and repeats until the end.
