# ip_address_utils.py
# Utility functions for IP address manipulation and subnet calculations
# Designed for learning Network Layer concepts and research applications


def ip_to_binary(ip):
    """
    Convert an IPv4 address to binary format.

    Args:
        ip (str): IPv4 address (e.g., '192.168.1.1')

    Returns:
        str: Binary representation (e.g., '11000000.10101000.00000001.00000001')
    """
    try:
        return ".".join(format(int(octet), "08b") for octet in ip.split("."))
    except ValueError:
        return "Invalid IP address format"


def subnet_hosts(mask):
    """
    Calculate the number of usable hosts in a subnet.

    Args:
        mask (int): Subnet mask bits (e.g., 24 for /24)

    Returns:
        int: Number of usable hosts (excludes network and broadcast addresses)
    """
    if not 0 <= mask <= 32:
        return "Invalid subnet mask"
    return 2 ** (32 - mask) - 2


def subnet_range(ip, mask):
    """
    Calculate the address range for a given IP and subnet mask.

    Args:
        ip (str): IPv4 address (e.g., '192.168.1.0')
        mask (int): Subnet mask bits (e.g., 24)

    Returns:
        tuple: (network address, first host, last host, broadcast address)
    """
    try:
        octets = [int(o) for o in ip.split(".")]
        binary_ip = "".join(format(o, "08b") for o in octets)
        network_bits = binary_ip[:mask].ljust(32, "0")
        network_octets = [int(network_bits[i : i + 8], 2) for i in range(0, 32, 8)]
        broadcast_bits = binary_ip[:mask].ljust(32, "1")
        broadcast_octets = [int(broadcast_bits[i : i + 8], 2) for i in range(0, 32, 8)]
        first_host = network_octets[:]
        first_host[3] += 1
        last_host = broadcast_octets[:]
        last_host[3] -= 1
        return (
            ".".join(map(str, network_octets)),
            ".".join(map(str, first_host)),
            ".".join(map(str, last_host)),
            ".".join(map(str, broadcast_octets)),
        )
    except ValueError:
        return "Invalid IP or mask"


# Example usage
if __name__ == "__main__":
    ip = "192.168.1.1"
    mask = 24
    print(f"IP {ip} in binary: {ip_to_binary(ip)}")
    print(f"Hosts in /{mask}: {subnet_hosts(mask)}")
    print(f"Subnet range for {ip}/{mask}: {subnet_range('192.168.1.0', mask)}")
