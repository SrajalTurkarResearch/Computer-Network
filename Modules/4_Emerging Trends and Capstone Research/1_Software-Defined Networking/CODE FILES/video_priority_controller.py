# video_priority_controller.py
# Ryu SDN controller that prioritizes UDP packets (e.g., for video calls).
# Purpose: Demonstrate SDN’s ability to optimize specific traffic types.
# Requirements: Install Ryu (`pip install ryu`) and Mininet (`sudo apt-get install mininet`).
# Usage: Run with `ryu-manager video_priority_controller.py` and start Mininet:
# `sudo mn --topo=linear,3 --controller=remote`

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3


class VideoPrioritySwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, MAIN_DISPATCHER)
    def switch_features_handler(self, ev):
        """Handle switch connection and install rules."""
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # Rule 1: Prioritize UDP packets (e.g., Zoom on port 8801)
        match_udp = parser.OFPMatch(ip_proto=17, udp_dst=8801)
        actions = [parser.OFPActionOutput(ofproto.OFPP_NORMAL)]
        self.add_flow(datapath, 10, match_udp, actions)

        # Rule 2: Default rule for other packets
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        """Add a flow entry to the switch."""
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(
            datapath=datapath, priority=priority, match=match, instructions=inst
        )
        datapath.send_msg(mod)


# Notes for scientists:
# - Test with Mininet: Use `iperf -u -p 8801` to simulate UDP traffic.
# - Research idea: Add QoS (Quality of Service) rules to limit bandwidth for non-priority traffic.
# - Extend to prioritize other protocols (e.g., TCP for web traffic).
