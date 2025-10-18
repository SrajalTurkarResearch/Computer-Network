# Case Studies in Routing Protocols: OSPF, BGP, and Convergence

This document presents six real-world and hypothetical case studies to illustrate the practical applications, challenges, and research opportunities of OSPF, BGP, and routing convergence. Designed for aspiring network scientists, each case includes technical details, impacts, lessons, and a research question to inspire innovation. These cases address gaps in standard tutorials, such as protocol interactions and security vulnerabilities, grounding theory in real events from 2008 to 2025.

## Case Study 1: BGP Asymmetric Routing (2025 Hypothetical)

**Context** : In 2025, a Tier-1 ISP (AS100) misconfigured BGP policies, setting Local Preference to 200 for inbound traffic from AS200 (content provider) but 50 for outbound traffic, causing asymmetric routing.
**Technical Details** :

- AS100 received prefix 8.8.8.0/24 from AS200 (direct path, LocalPref=200) and AS300 (via AS200, LocalPref=100). It chose the direct path for inbound.
- Outbound traffic used a different path (AS100→AS300→AS200) due to lower LocalPref, increasing latency by 50ms.
- Traceroute revealed inconsistent paths, complicating debugging.
  **Impact** : Users experienced jitter in video calls and gaming, costing the ISP customer trust.
  **Lessons Learned** :
- Align inbound/outbound policies to avoid asymmetry.
- Use monitoring tools (e.g., BGPmon) to detect path mismatches.
- Test configurations in a lab (e.g., GNS3) before deployment.
  **Research Question** : How can AI predict and mitigate asymmetric routing in real-time using BGP attributes?
  **Source** : Hypothetical based on 2025 ISP trends and common BGP issues.

## Case Study 2: BGP Route Hijack – YouTube (2008)

**Context** : Pakistan Telecom (AS17557) attempted to block YouTube locally by advertising its prefix (208.65.153.0/24) but inadvertently propagated it globally.
**Technical Details** :

- AS17557 announced the prefix via eBGP, with a shorter AS-Path than YouTube’s (AS36561).
- Global routers preferred the hijacked path, redirecting YouTube traffic to Pakistan.
- No RPKI or prefix filtering was widely deployed in 2008, allowing the error to spread.
  **Impact** : YouTube was unreachable globally for ~2 hours, affecting millions of users.
  **Lessons Learned** :
- Implement prefix filtering to reject invalid advertisements.
- Adopt RPKI to verify prefix ownership.
- Monitor BGP updates for anomalies (e.g., sudden prefix changes).
  **Research Question** : Can machine learning detect BGP hijacks faster than RPKI, using real-time AS-Path analysis?
  **Source** : Public reports, RIPE NCC analysis (2008).

## Case Study 3: Cloudflare Outage – BGP Convergence Delay (2020)

**Context** : Cloudflare’s misconfiguration triggered a BGP update cascade, delaying convergence.
**Technical Details** :

- A router withdrew prefixes for 50% of Cloudflare’s services (e.g., 1.1.1.1/24).
- eBGP updates propagated across ASes, taking 27 seconds to stabilize due to long AS-Paths and policy reevaluations.
- No loop issues, but slow convergence caused packet loss.
  **Impact** : Half of Cloudflare’s services (DNS, CDN) were down for 27 seconds, disrupting websites globally.
  **Lessons Learned** :
- Optimize BGP timers (e.g., MRAI) for faster convergence.
- Use redundant peerings to minimize disruption.
- Simulate large-scale updates in tools like ns-3 to predict delays.
  **Research Question** : Can formal verification (e.g., TLA+) predict BGP convergence delays under specific topologies?
  **Source** : Cloudflare post-mortem blog (July 2020).

## Case Study 4: Facebook Outage – BGP/OSPF Interaction Failure (2021)

**Context** : A configuration error in Facebook’s backbone caused BGP to withdraw prefixes, and OSPF failed to recover internally.
**Technical Details** :

- BGP routers announced WITHDRAW for Facebook’s prefixes (e.g., 157.240.0.0/16).
- OSPF, running internally, didn’t redistribute alternative paths due to misconfigured route maps.
- Lack of monitoring for protocol interactions led to a 6-hour outage.
  **Impact** : Facebook, WhatsApp, and Instagram were offline, costing billions in revenue and user trust.
  **Lessons Learned** :
- Test BGP-OSPF redistribution in a lab to avoid loops.
- Monitor inter-protocol dependencies with tools like NetFlow.
- Implement redundant internal paths (e.g., multi-area OSPF).
  **Research Question** : How can formal models (e.g., Coq) verify BGP-OSPF interactions to prevent outages?
  **Source** : Facebook engineering blog (October 2021).

## Case Study 5: RPKI Deployment Flaws (2023)

**Context** : An ISP’s RPKI validator software had a bug, rejecting valid BGP routes.
**Technical Details** :

- RPKI uses Route Origin Authorization (ROA) to verify prefix ownership.
- A software update misparsed ROAs, dropping routes for 10% of prefixes (e.g., 172.16.0.0/12).
- BGP routers fell back to less optimal paths, increasing latency by 20ms.
  **Impact** : Affected ISPs saw degraded performance for hours until patched.
  **Lessons Learned** :
- Test RPKI validators rigorously in staging environments.
- Maintain fallback routes during validation failures.
- Monitor RPKI drop rates with tools like RIPEstat.
  **Research Question** : Can blockchain-based systems replace RPKI for more reliable prefix validation?
  **Source** : Routing security forums, RIPE NCC reports (2023).

## Case Study 6: OSPF Scalability in Data Centers (2024)

**Context** : A hyperscale data center (e.g., Google) faced OSPF scalability issues during rapid expansion.
**Technical Details** :

- OSPF’s Link-State Database (LSDB) grew to 10,000 LSAs, overwhelming router memory.
- Frequent topology changes (e.g., server additions) triggered SPF recomputations, delaying convergence to 2 seconds.
- Multi-area OSPF reduced LSDB size but complicated troubleshooting.
  **Impact** : Intermittent packet loss disrupted cloud services for milliseconds.
  **Lessons Learned** :
- Use stub areas or BGP for large-scale data centers.
- Optimize SPF timers to balance stability and speed.
- Monitor LSDB size with tools like SolarWinds.
  **Research Question** : Can AI optimize OSPF area design for hyperscale networks dynamically?
  **Source** : Hypothetical based on 2024 data center trends.

These case studies bridge theory and practice, highlighting challenges (security, scalability, interactions) and opportunities for innovation in routing protocols.
