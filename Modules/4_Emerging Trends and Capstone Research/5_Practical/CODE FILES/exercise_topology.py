# exercise_topology.py
# Purpose: Create a Mininet topology with 3 hosts and 2 switches for an exercise,
# demonstrating SDN connectivity testing. This builds on SDN principles by
# scaling the topology from simple_sdn.py.
# Usage: Run with `sudo python3 exercise_topology.py` in a Ubuntu environment
# with Mininet installed. Start Ryu in another terminal:
# `ryu-manager ryu.app.simple_switch_13`. Test with `h1 ping h3` in Mininet CLI.
# Learning Objective: Practice building and testing SDN topologies, preparing
# for complex prototyping and research.

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


def exercise_topology():
    # Initialize Mininet with controller and Open vSwitch
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Add controller
    c0 = net.addController("c0")

    # Add two switches
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    # Add three hosts
    h1 = net.addHost("h1")
    h2 = net.addHost("h2")
    h3 = net.addHost("h3")

    # Connect hosts and switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, s2)
    net.addLink(h3, s2)

    # Start the network
    net.start()

    # Instruct user to start Ryu
    print("Run in another terminal: ryu-manager ryu.app.simple_switch_13")

    # Open CLI for testing
    CLI(net)

    # Clean up
    net.stop()


if __name__ == "__main__":
    # Set logging for debugging
    setLogLevel("info")
    exercise_topology()

# Notes for Aspiring Scientist:
# - This topology tests connectivity across two switches, showing how SDN
#   controllers manage multi-hop paths.
# - Experiment: Use `h1 ping h3` and `h2 ping h3`. Measure latency with `ping -c 4`.
# - Research Idea: Add a third switch and hypothesize how path length affects
#   performance. Test with iperf for throughput (`h1 iperf -s; h3 iperf -c h1`).
