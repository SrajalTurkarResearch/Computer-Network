# simple_switch.py
# A basic Ryu SDN controller that forwards all packets to the controller for processing.
# Purpose: Introduce SDN controller programming for beginners.
# Requirements: Install Ryu (`pip install ryu`) and Mininet (`sudo apt-get install mininet`).
# Usage: Run with `ryu-manager simple_switch.py` and start Mininet in another terminal:
# `sudo mn --topo=linear,3 --controller=remote`

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3


class SimpleSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, MAIN_DISPATCHER)
    def switch_features_handler(self, ev):
        """Handle switch connection and install default rule."""
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        # Default rule: Send all packets to controller
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
# - Test with Mininet: `pingall` to check connectivity.
# - Extend by adding specific flow rules (e.g., match IP or port).
# - Research idea: Log packet counts for traffic analysis.
