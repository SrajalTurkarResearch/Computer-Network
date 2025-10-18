# bell_lapadula_model.py
# Purpose: Simulates the Bell-LaPadula model for confidentiality in formal security.
# Use: Run to check read/write access based on security levels.
# Relevance: Understand how formal models ensure data security, a key research area.
# Requirements: Python 3 (no external libraries needed).

# Define security levels (like a ladder: higher number = more secure)
levels = {"Unclassified": 0, "Secret": 1, "Top Secret": 2}


def can_read(user_level, file_level):
    """
    Check if a user can read a file (no read up).
    Args:
        user_level (str): User's security level.
        file_level (str): File's security level.
    Returns:
        bool: True if allowed, False otherwise.
    """
    return levels[user_level] >= levels[file_level]


def can_write(user_level, file_level):
    """
    Check if a user can write to a file (no write down).
    Args:
        user_level (str): User's security level.
        file_level (str): File's security level.
    Returns:
        bool: True if allowed, False otherwise.
    """
    return levels[user_level] <= levels[file_level]


if __name__ == "__main__":
    # Test access rules
    print(
        "Can Secret user read Unclassified file?", can_read("Secret", "Unclassified")
    )  # True
    print(
        "Can Secret user read Top Secret file?", can_read("Secret", "Top Secret")
    )  # False
    print(
        "Can Secret user write to Top Secret file?", can_write("Secret", "Top Secret")
    )  # True
    print(
        "Can Secret user write to Unclassified file?",
        can_write("Secret", "Unclassified"),
    )  # False

    # Exercise: Add a new level (e.g., 'Confidential' = 0.5) and test access rules.
    # How does this change the lattice?

# Why This Matters for Scientists:
# - Models like Bell-LaPadula are used in secure systems; this code helps you test them.
# - Extend to research lattice-based access control or formal verification.
