# slicing_controller.py
# Purpose: Ryu controller for 5G network slicing in network_slicing_5g.py. It
# assigns flows to IoT or video slices based on source/destination IPs, enforcing
# QoS policies. Demonstrates SDN’s role in 5G customization.
# Usage: Run with `ryu-manager slicing_controller.py` while network_slicing_5g.py
# is running. Requires Ryu (`pip3 install ryu`).
# Learning Objective: Learn how SDN controllers implement network slicing by
# programming flow rules for different services.

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ipv4


class SlicingController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SlicingController, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        # Define slices by IP pairs (simplified)
        self.slices = {
            ("10.0.0.1", "10.0.0.3"): "iot",  # h1-h3
            ("10.0.0.2", "10.0.0.4"): "video",  # h2-h4
        }

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        match = parser.OFPMatch()
        actions = [
            parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)
        ]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(
            datapath=datapath, priority=priority, match=match, instructions=inst
        )
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
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
        ip_pkt = pkt.get_protocols(ipv4.ipv4)

        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})
        self.mac_to_port[dpid][src] = in_port

        # Determine slice based on IP
        out_port = None
        if ip_pkt:
            src_ip = ip_pkt[0].src
            dst_ip = ip_pkt[0].dst
            slice_type = self.slices.get((src_ip, dst_ip), "default")

            # Assign ports based on slice (simplified: use port 2 for IoT, 3 for video)
            if slice_type == "iot":
                out_port = 2  # Low-bandwidth path
            elif slice_type == "video":
                out_port = 3  # High-bandwidth path
            else:
                out_port = ofproto.OFPP_FLOOD  # Default

        if out_port and dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]

        # Install flow rule
        actions = [parser.OFPActionOutput(out_port)]
        match = parser.OFPMatch(
            in_port=in_port, eth_dst=dst, ipv4_src=src_ip, ipv4_dst=dst_ip
        )
        self.add_flow(datapath, 1, match, actions)

        # Send packet
        out = parser.OFPPacketOut(
            datapath=datapath,
            buffer_id=msg.buffer_id,
            in_port=in_port,
            actions=actions,
            data=msg.data,
        )
        datapath.send_msg(out)


# Notes for Aspiring Scientist:
# - This controller assigns flows to slices based on IP addresses, simulating 5G
#   network slicing for different QoS needs.
# - Experiment: Add QoS policies (e.g., rate limiting for IoT) using OpenFlow meters.
# - Research Idea: Hypothesize that slicing reduces video jitter by 20%. Test with
#   `iperf -u` for UDP traffic and analyze.
# - Real-World Connection: 5G providers like AT&T use SDN/NFV for slicing to support
#   diverse applications (e.g., IoT, AR/VR).
