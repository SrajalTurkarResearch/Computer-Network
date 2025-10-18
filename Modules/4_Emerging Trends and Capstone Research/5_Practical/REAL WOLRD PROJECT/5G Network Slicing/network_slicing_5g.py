# network_slicing_5g.py
# Purpose: Simulate 5G network slicing using Mininet and Ryu. The topology includes
# 4 hosts and 2 switches, with two slices: one for low-bandwidth IoT (e.g., sensors)
# and one for high-bandwidth video. This demonstrates SDN/NFV’s role in 5G networks.
# Usage: Run with `sudo python3 network_slicing_5g.py` in a Ubuntu environment with
# Mininet and Ryu installed. Start Ryu controller in another terminal:
# `ryu-manager slicing_controller.py`.
# Test with: `h1 iperf -c h3 -t 10` (IoT slice), `h2 iperf -c h4 -t 10` (video slice).
# Learning Objective: Understand how SDN enables network slicing for customized QoS,
# a key feature in 5G networks like Verizon’s.

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink


def network_slicing_5g():
    # Initialize Mininet with bandwidth-limited links
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)

    # Add controller
    c0 = net.addController("c0")

    # Add switches
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    # Add hosts: h1,h3 for IoT slice; h2,h4 for video slice
    h1 = net.addHost("h1")  # IoT source
    h2 = net.addHost("h2")  # Video source
    h3 = net.addHost("h3")  # IoT destination
    h4 = net.addHost("h4")  # Video destination

    # Connect with bandwidth limits: IoT (1 Mbps), Video (10 Mbps)
    net.addLink(h1, s1, bw=1)  # IoT slice, low bandwidth
    net.addLink(h2, s1, bw=10)  # Video slice, high bandwidth
    net.addLink(s1, s2, bw=10)  # Core link
    net.addLink(h3, s2, bw=1)
    net.addLink(h4, s2, bw=10)

    # Start network
    net.start()

    # Instruct user to start Ryu controller
    print("Run in another terminal: ryu-manager slicing_controller.py")

    # Open CLI for testing
    CLI(net)

    # Clean up
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    network_slicing_5g()

# Notes for Aspiring Scientist:
# - This topology creates two slices: IoT (h1-h3, low bandwidth) and video (h2-h4, high bandwidth).
# - Experiment: Use `iperf` to measure throughput for each slice and compare QoS.
# - Research Idea: Hypothesize that slicing improves video throughput by 30% over
#   unsliced networks. Test with `iperf` and analyze jitter.
# - Real-World Connection: Verizon uses SDN/NFV for 5G slicing, enabling low-latency
#   AR/VR applications.
