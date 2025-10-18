# simple_sdn.py
# Purpose: Create a simple SDN topology using Mininet with 2 hosts and 1 switch,
# controlled by a Ryu SDN controller. This demonstrates the separation of control
# plane (Ryu) and data plane (Mininet switches), a core SDN concept.
# Usage: Run this script with `sudo python3 simple_sdn.py` in a Ubuntu environment
# with Mininet installed. In a separate terminal, start Ryu with:
# `ryu-manager ryu.app.simple_switch_13`.
# In Mininet CLI, test connectivity with: `h1 ping h2`.
# Prerequisites: Install Mininet (`sudo apt install mininet`) and Ryu (`pip3 install ryu`).
# Learning Objective: Understand how SDN controllers program switches to forward packets.

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


def simple_sdn():
    # Initialize Mininet with a controller and Open vSwitch
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Add a remote controller (Ryu will connect here)
    c0 = net.addController("c0")

    # Add one switch (data plane device)
    s1 = net.addSwitch("s1")

    # Add two hosts (end devices)
    h1 = net.addHost("h1")
    h2 = net.addHost("h2")

    # Connect hosts to switch (links are virtual)
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start the network
    net.start()

    # Inform user to start Ryu controller in another terminal
    print("Run in another terminal: ryu-manager ryu.app.simple_switch_13")

    # Open Mininet CLI for interaction (e.g., ping tests)
    CLI(net)

    # Clean up when done
    net.stop()


if __name__ == "__main__":
    # Set logging to info level for debugging
    setLogLevel("info")
    simple_sdn()

# Notes for Aspiring Scientist:
# - This script creates a topology where the Ryu controller programs the switch
#   using OpenFlow protocol (southbound interface).
# - Experiment: In Mininet CLI, try `h1 ping h2` to see packets flow.
# - Research Idea: Modify the topology (add hosts/switches) and measure latency
#   using `ping -c 4 h1 h2`. Hypothesize: Does adding switches increase delay?
