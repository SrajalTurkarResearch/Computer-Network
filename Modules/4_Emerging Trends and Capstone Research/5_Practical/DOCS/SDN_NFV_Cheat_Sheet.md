# SDN/NFV Tutorial Cheat Sheet

This cheat sheet is your quick guide to learning Software-Defined Networking (SDN) and Network Function Virtualization (NFV) for prototyping next-generation networks. It summarizes the tutorial’s key points, tools, and code snippets in simple language, perfect for a beginner scientist. Use it to revise concepts, run prototypes, and plan research.

## 1. Computer Network Basics

- **Definition** : Connects devices to share data (e.g., files, messages). Like roads linking houses.
- **Types** :
- LAN: Small, like home Wi-Fi (<1ms latency).
- WAN: Big, like the internet.
- MAN: City-wide. PAN: Personal (Bluetooth).
- **Parts** :
- Hosts: Computers/phones with MAC/IP addresses.
- Switches: Connect in LAN (MAC-based).
- Routers: Link networks (IP-based).
- Protocols: TCP/IP (TCP reliable, UDP fast).
- **Data Flow** : Packets (data chunks) with headers (addresses). Routers use Dijkstra’s algorithm:
- \( d(v) = \min(d(v), d(u) + w(u,v)) \)
- Example: A-B(2), A-C(5), B-D(1). Path A-B-D, cost 3.

## 2. Why SDN/NFV? (Old Network Problems)

- **Issues** : Vendor lock-in (special hardware), manual setup (errors), hard to scale (\( O(n^2) \) links), inflexible.
- **Need** : 5G/6G needs <1ms latency, 75B IoT devices by 2025.

## 3. SDN Basics

- **Definition** : Separates control plane (decisions) from data plane (forwarding). Controller programs switches.
- **Architecture** :
- Application: Apps (e.g., load balancing).
- Control: Controller (e.g., Ryu).
- Data: Switches (OpenFlow).
- **Math** : Min cost = \( \sum c_p x_p \), \( x_p \in \{0,1\} \).
- **Tools** : Mininet (emulation), Ryu (controller), Open vSwitch.

## 4. NFV Basics

- **Definition** : Runs network jobs (e.g., firewalls) as software on normal computers.
- **Architecture** :
- VNFs: Virtual routers/firewalls.
- NFVI: Hardware/virtual resources.
- MANO: Plans (NFVO), manages (VNFM), allocates (VIM).
- **Math** : Max utility = \( \sum u_i x_i \), CPU \( \sum r_i x_i \leq R \).
- **Tools** : OpenStack (VIM), OSM (MANO).

## 5. SDN + NFV

- **Synergy** : SDN routes through NFV functions (service chaining).
- **Example** : 5G slicing for IoT (low bandwidth) vs. video (high bandwidth).

## 6. Tools and Setup

- **Install** :

```bash
  sudo apt update
  sudo apt install -y mininet python3-pip openvswitch-switch
  pip3 install ryu matplotlib networkx numpy
```

- **Mininet** : Emulates networks. Run: `sudo mn`.
- **Ryu** : SDN controller. Run: `ryu-manager ryu.app.simple_switch_13`.
- **OpenStack** : NFV infrastructure (install via DevStack).

## 7. Key Code Snippets

- **Simple SDN Topology** (`simple_sdn.py`):

  ```python
  from mininet.net import Mininet
  from mininet.node import Controller, OVSSwitch
  from mininet.cli import CLI
  from mininet.log import setLogLevel

  def simple_sdn():
      net = Mininet(controller=Controller, switch=OVSSwitch)
      c0 = net.addController('c0')
      s1 = net.addSwitch('s1')
      h1 = net.addHost('h1')
      h2 = net.addHost('h2')
      net.addLink(h1, s1)
      net.addLink(h2, s1)
      net.start()
      print("Run: ryu-manager ryu.app.simple_switch_13")
      CLI(net)
      net.stop()

  if __name__ == '__main__':
      setLogLevel('info')
      simple_sdn()
  ```

- **Visualize Topology** (`network_visualization.py`):
  ```python
  import networkx as nx
  import matplotlib.pyplot as plt
  G = nx.Graph()
  G.add_nodes_from(['h1', 'h2', 's1'])
  G.add_edges_from([('h1', 's1'), ('h2', 's1')])
  plt.figure(figsize=(6,4))
  nx.draw(G, with_labels=True, node_color='lightblue')
  plt.title('Simple SDN Topology')
  plt.show()
  ```
- **Load Balancer** (`sdn_load_balancer.py`): 3 hosts, 2 switches, balance traffic.
- **5G Slicing** (`network_slicing_5g.py`): 4 hosts, 2 switches, IoT/video slices.

## 8. Real-World Cases

- **Google B4** : SDN for data centers, 70% link use.
- **Verizon 5G** : SDN/NFV for slicing, <1ms latency.
- **AT&T** : Fast service setup with SDN/NFV.

## 9. Research Prompts

- **SDN** : Test if load balancing cuts latency by 20%. Use `iperf` in Mininet.
- **NFV** : Hypothesize VNFs save 30% energy. Simulate in OpenStack.
- **6G** : Explore AI for slice optimization in terahertz bands.

## 10. Quick Tips

- **Test Connectivity** : `h1 ping h2` in Mininet CLI.
- **Measure Throughput** : `h1 iperf -c h2 -t 10`.
- **Visualize** : Draw topologies (circles for hosts/switches, lines for links).
- **Read** : IEEE NFV-SDN papers for advanced ideas.

## 11. Common Mistakes

- Forgetting `sudo` for Mininet.
- Not starting Ryu controller before testing.
- Ignoring QoS in slicing (use bandwidth limits in `TCLink`).

## 12. Next Steps

- Learn P4 for programmable switches.
- Prototype 6G slicing with ONOS.
- Publish findings on arXiv.

This cheat sheet is your go-to reference for SDN/NFV. Keep it handy for quick checks while prototyping or researching!
