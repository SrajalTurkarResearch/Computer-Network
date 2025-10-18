# CRC Error Detection for Data Link Layer
# Created by Grok 4, xAI, for aspiring scientists and researchers
# Date: September 09, 2025
#
# Purpose: Implement Cyclic Redundancy Check (CRC) for error detection.
# Theory: Treat data as a polynomial, divide by a generator polynomial
# (e.g., 1011 = x^3 + x + 1), append remainder. Receiver checks if
# division yields zero remainder. Detects bursts up to deg(generator).
#
# Why: Ensures data integrity in noisy channels (e.g., Mars rover images).
# Research: Test different generators or burst errors.
#
# Dependencies: None (pure Python).


def crc_divide(data, generator):
    """
    Perform CRC division (modulo-2 arithmetic, i.e., XOR).
    Parameters:
        data (list): Binary data as list of 0s and 1s.
        generator (list): Generator polynomial (e.g., [1,0,1,1] for x^3 + x + 1).
    Returns:
        remainder (list): CRC remainder to append.
    """
    # Extend data with zeros (degree of generator - 1)
    extended = data + [0] * (len(generator) - 1)
    for i in range(len(data)):
        if extended[i] == 1:
            for j in range(len(generator)):
                extended[i + j] ^= generator[j]  # XOR
    return extended[-(len(generator) - 1) :]


def crc_check(received, generator):
    """
    Check if received data (with CRC) is error-free.
    Parameters:
        received (list): Data + CRC.
        generator (list): Same generator used for encoding.
    Returns:
        bool: True if no error (remainder zero), False otherwise.
    """
    remainder = crc_divide(received, generator)
    return all(bit == 0 for bit in remainder)


if __name__ == "__main__":
    # Example: Data = 110101, Generator = 1011
    data = [1, 1, 0, 1, 0, 1]
    generator = [1, 0, 1, 1]

    # Compute CRC and append
    crc = crc_divide(data, generator)
    sent = data + crc
    print(f"Original Data: {data}")
    print(f"CRC: {crc}")
    print(f"Sent Frame: {sent}")

    # Check with no error
    is_valid = crc_check(sent, generator)
    print(f"No Error Check: {'Valid' if is_valid else 'Error'}")

    # Introduce error (flip bit at index 2)
    received = sent.copy()
    received[2] = 1 - received[2]
    is_valid = crc_check(received, generator)
    print(f"With Error (bit 2 flipped): {'Valid' if is_valid else 'Error'}")

    # Research Extension: Test with burst errors (flip 2-3 consecutive bits)
    # or try generators like CRC-32 ([1,0,0,0,...,1]).
