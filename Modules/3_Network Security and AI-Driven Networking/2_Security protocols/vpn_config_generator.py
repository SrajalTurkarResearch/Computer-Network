# vpn_config_generator.py
# Purpose: Generates a basic OpenVPN configuration file for learning VPN setup.
# Use: Run to print a sample OpenVPN client config; save to .ovpn for real use.
# Relevance: Understand how VPNs use TLS/SSL for secure tunneling, a key application.
# Requirements: Python 3 (no external libraries needed).
# Note: This is a conceptual generator; real VPN setup requires certificates and server.


def generate_vpn_config():
    """
    Generate a sample OpenVPN client configuration.
    Returns:
        str: Configuration text for an OpenVPN client.
    """
    config = """
# Sample OpenVPN Client Configuration
client
dev tun
proto udp
remote vpn.example.com 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert client.crt
key client.key
remote-cert-tls server
cipher AES-256-GCM
"""
    return config


if __name__ == "__main__":
    # Generate and print the config
    config = generate_vpn_config()
    print("Sample OpenVPN Config:")
    print(config)

    # Optional: Save to a file
    with open("client.ovpn", "w") as f:
        f.write(config)
    print("Config saved to client.ovpn")

    # Exercise: Modify the config to use TCP instead of UDP (change 'proto udp' to 'proto tcp').
    # Research how protocol choice affects performance.

# Why This Matters for Scientists:
# - Shows how VPNs configure TLS-based security, linking to real-world remote access.
# - Experiment with configs to explore scalability or protocol choices for research.
