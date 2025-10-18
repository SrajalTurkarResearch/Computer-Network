# sdn_load_balancer.py
# Purpose: Implement a simple SDN load balancer using Mininet and Ryu. The topology
# includes 3 hosts and 2 switches, with the Ryu controller distributing traffic
# across two paths to balance load. This demonstrates SDN's centralized control
# for optimizing network performance, as seen in real-world cases like Google's B4.
# Usage: Run with `sudo python3 sdn_load_balancer.py` in a Ubuntu environment with
# Mininet and Ryu installed (`sudo apt install mininet`, `pip3 install ryu`).
# In a separate terminal, start Ryu with the custom controller:
# `ryu-manager load_balancer_controller.py`.
# Test with Mininet CLI: `h1 iperf -c h3 -t 10` to measure throughput.
# Learning Objective: Understand how SDN controllers program flow rules to balance
# traffic, a key feature for next-generation networks.

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


def sdn_load_balancer():
    # Initialize Mininet with a remote controller and Open vSwitch
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Add controller (Ryu will connect)
    c0 = net.addController("c0")

    # Add switches
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    # Add hosts
    h1 = net.addHost("h1")  # Source
    h2 = net.addHost("h2")  # Intermediate
    h3 = net.addHost("h3")  # Destination

    # Create topology: h1 -> s1 -> s2 -> h3, with h2 as alternate path
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, s2)
    net.addLink(h2, s2)
    net.addLink(s2, h3)

    # Start network
    net.start()

    # Instruct user to start custom Ryu controller
    print("Run in another terminal: ryu-manager load_balancer_controller.py")

    # Open CLI for testing
    CLI(net)

    # Clean up
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    sdn_load_balancer()

# Notes for Aspiring Scientist:
# - This topology allows the Ryu controller to distribute traffic from h1 to h3
#   via two paths (s1-s2 or s1-h2-s2), mimicking load balancing in real SDN networks.
# - Experiment: Use `iperf` to measure throughput (`h1 iperf -c h3 -t 10`).
#   Compare with and without load balancing.
# - Research Idea: Hypothesize that load balancing reduces latency by 20%.
#   Measure with `ping -c 10 h1 h3` and analyze variance.
# - Real-World Connection: Google’s B4 uses SDN to achieve 70% link utilization
#   by balancing traffic dynamically.
