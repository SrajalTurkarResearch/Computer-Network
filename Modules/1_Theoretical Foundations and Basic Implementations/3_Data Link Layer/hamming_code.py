# Hamming Code for Error Correction in Data Link Layer
# Created by Grok 4, xAI, for aspiring scientists and researchers
# Date: September 09, 2025
#
# Purpose: Implement Hamming Code for single-error correction.
# Theory: Add r parity bits at positions 2^i (1,2,4,8,...).
# Each parity checks bits where position's binary has 1 in i-th bit.
# Syndrome (from failed checks) gives error position in binary.
# Derivation: Hamming distance d=3 corrects 1 error (2^r >= m+r+1).
#
# Why: Critical for low-latency links (e.g., satellites, DNA storage).
# Research: Extend to multi-bit errors or quantum codes.
#
# Dependencies: None (pure Python).


def hamming_encode(data):
    """
    Encode data with Hamming Code.
    Parameters:
        data (list): Binary data as 0s and 1s.
    Returns:
        code (list): Encoded data with parity bits.
    """
    m = len(data)
    # Find r: 2^r >= m + r + 1
    r = 0
    while (1 << r) < m + r + 1:
        r += 1
    code = [0] * (m + r)
    # Place data bits (skip power-of-2 positions)
    j = 0
    for i in range(1, m + r + 1):
        if i & (i - 1) != 0:  # Not a power of 2
            code[i - 1] = data[j]
            j += 1
    # Compute parity bits
    for i in range(r):
        pos = 1 << i  # 1, 2, 4, ...
        parity = 0
        for j in range(1, m + r + 1):
            if j & pos:
                parity ^= code[j - 1]
        code[pos - 1] = parity
    return code


def hamming_decode(code):
    """
    Decode and correct single-bit error.
    Parameters:
        code (list): Received Hamming code.
    Returns:
        corrected (list): Code with error fixed (if any).
        syndrome (int): Error position (0 if no error).
    """
    n = len(code)
    r = 0
    while (1 << r) < n + 1:
        r += 1
    syndrome = 0
    for i in range(r):
        pos = 1 << i
        parity = 0
        for j in range(1, n + 1):
            if j & pos:
                parity ^= code[j - 1]
        if parity:
            syndrome |= pos
    if syndrome:
        code[syndrome - 1] = 1 - code[syndrome - 1]
    return code, syndrome


if __name__ == "__main__":
    # Example: Data = 1011
    data = [1, 0, 1, 1]
    encoded = hamming_encode(data)
    print(f"Original Data: {data}")
    print(f"Encoded (p1,p2,d1,p4,d2,d3,d4): {encoded}")

    # Introduce error at position 5 (1-based, d2)
    received = encoded.copy()
    received[4] = 1 - received[4]
    print(f"Received with Error (pos 5): {received}")

    # Decode and correct
    corrected, syndrome = hamming_decode(received)
    print(f"Syndrome: {syndrome} (points to pos 5)")
    print(f"Corrected Code: {corrected}")

    # Verify data extraction
    m = len(data)
    r = int(len(corrected) - m)
    extracted = [
        corrected[i - 1] for i in range(1, len(corrected) + 1) if i & (i - 1) != 0
    ]
    print(f"Extracted Data: {extracted}")

    # Research Extension: Test with multiple errors (Hamming fails),
    # or implement Reed-Solomon for burst errors.
