# network_simulation.py
# Purpose: Simulate a simple network using Mininet.
# Context: Part of Jupyter Notebook tutorial, Section 4 - Network Simulation.
# Use: Run on Linux with Mininet installed (`sudo apt install mininet`).
# Note: Requires sudo privileges (`sudo python3 network_simulation.py`).

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel
import time


def create_simple_network():
    """
    Create a network with 2 hosts and 1 switch.
    Theory Link: Section 4.2 - Network Simulation in Jupyter Notebook.
    Analogy: Like building a toy city to test traffic flow.
    """
    # Initialize Mininet
    net = Mininet(controller=Controller)

    try:
        # Add hosts (computers), switch, and controller
        print("Creating network...")
        h1 = net.addHost("h1")
        h2 = net.addHost("h2")
        s1 = net.addSwitch("s1")
        c0 = net.addController("c0")

        # Add links with bandwidth limit
        net.addLink(h1, s1, bw=10)  # 10 Mbps
        net.addLink(h2, s1)

        # Start the network
        net.start()
        print("Network started. Topology: h1 --- s1 --- h2")

        # Test connectivity with ping
        print("\nTesting connectivity (ping h1 to h2)...")
        result = net.ping([h1, h2])
        print(f"Ping result: {result}")

        # Open CLI for manual testing
        print("\nEntering Mininet CLI. Try 'h1 ping h2' or 'exit' to quit.")
        CLI(net)

    except Exception as e:
        print(f"Simulation error: {e}")
    finally:
        # Clean up
        net.stop()
        print("Network stopped.")


if __name__ == "__main__":
    print("Network Simulation Demo for Network Scientists")
    print("=========================================")
    setLogLevel("info")  # Show Mininet logs
    create_simple_network()

    # Research Tip: Add congestion (e.g., `tc qdisc add dev s1-eth1 root tbf rate 1mbit latency 50ms`).
    # See Jupyter Notebook Section 4 for large-scale simulations or NS-3.
