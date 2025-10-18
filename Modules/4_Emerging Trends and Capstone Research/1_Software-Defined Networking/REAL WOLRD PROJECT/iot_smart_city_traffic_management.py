# iot_smart_city_traffic_management.py
# Simulates SDN prioritizing IoT sensor traffic for a smart city network.
# Purpose: Show SDN's role in IoT, inspired by Singapore's smart city.
# Requirements: Install Ryu, Mininet (`pip install ryu`, `sudo apt-get install mininet`).
# Usage: Run with `ryu-manager iot_smart_city_traffic_management.py` and start Mininet:
# `sudo mn --topo=tree,depth=2,fanout=2 --controller=remote`

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3


class IoTSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, MAIN_DISPATCHER)
    def switch_features_handler(self, ev):
        """Handle switch connection and install rules for IoT traffic."""
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # Rule 1: Prioritize IoT sensor traffic (UDP, port 12345)
        match_iot = parser.OFPMatch(ip_proto=17, udp_dst=12345)
        actions = [parser.OFPActionOutput(ofproto.OFPP_NORMAL)]
        self.add_flow(datapath, 10, match_iot, actions)

        # Rule 2: Default rule for other traffic
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
# - Real-world impact: Singapore's SDN reduced traffic congestion by 15%.
# - Research idea: Add rules for disaster recovery (e.g., prioritize earthquake sensors).
# - Test in Mininet: Use `iperf -u -p 12345` to simulate IoT traffic.
