# load_balancer_controller.py
# Purpose: Ryu controller script to implement load balancing for the SDN topology
# in sdn_load_balancer.py. It adds flow rules to distribute traffic across two paths.
# Usage: Run with `ryu-manager load_balancer_controller.py` in a separate terminal
# while sdn_load_balancer.py is running. Requires Ryu (`pip3 install ryu`).
# Learning Objective: Learn how SDN controllers use OpenFlow to program switches
# for dynamic traffic management.

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
import random


class LoadBalancer(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(LoadBalancer, self).__init__(*args, **kwargs)
        self.mac_to_port = {}  # Store MAC-to-port mappings
        self.paths = {}  # Store path choices for load balancing

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        # Handle switch connection, install default flow
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # Install table-miss flow entry (send unknown packets to controller)
        match = parser.OFPMatch()
        actions = [
            parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)
        ]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        # Add a flow rule to the switch
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(
            datapath=datapath, priority=priority, match=match, instructions=inst
        )
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        # Handle incoming packets
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match["in_port"]

        # Parse packet
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        src = eth.src
        dst = eth.dst

        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})

        # Learn source MAC
        self.mac_to_port[dpid][src] = in_port

        # Choose path for destination (load balancing)
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            # Randomly select path for load balancing (simulate two paths)
            out_port = random.choice([2, 3])  # Assuming ports 2 and 3 lead to paths

        # Install flow rule
        actions = [parser.OFPActionOutput(out_port)]
        match = parser.OFPMatch(in_port=in_port, eth_dst=dst)
        self.add_flow(datapath, 1, match, actions)

        # Send packet out
        out = parser.OFPPacketOut(
            datapath=datapath,
            buffer_id=msg.buffer_id,
            in_port=in_port,
            actions=actions,
            data=msg.data,
        )
        datapath.send_msg(out)


# Notes for Aspiring Scientist:
# - This Ryu controller randomly selects paths for traffic, simulating load balancing.
# - Experiment: Modify to track path loads (e.g., packet counts) and choose least-loaded path.
# - Research Idea: Hypothesize that dynamic path selection improves throughput by 25%.
#   Test with `iperf` and compare against static routing.
# - Real-World Connection: AT&T uses SDN for dynamic traffic management in 5G networks.
