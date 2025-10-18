```markdown
# Case Studies in Routing Protocols

## Case Study 1: BGP Asymmetric Routing (2025)

**Context**: An ISP misconfigured BGP policies, setting different Local Preference values for inbound and outbound paths.  
**Issue**: Traffic from AS1 to AS2 took a direct path, but return traffic looped through AS3, causing delays.  
**Lesson**: Asymmetric routing complicates troubleshooting; align policies or use tools like traceroute to diagnose.  
**Source**: Hypothetical based on 2025 ISP trends.

## Case Study 2: BGP Vulnerabilities

**Context**: BGP relies on trust, making it prone to hijacks.  
**Issue**: Malicious ASes advertise false prefixes, redirecting traffic (e.g., cryptojacking in 2018).  
**Lesson**: Deploy RPKI to validate prefix ownership; BGPsec for path authentication.  
**Source**: Multiple incidents reported in routing security studies.

## Case Study 3: Cloudflare Outage (2020)

**Context**: BGP update propagation delayed convergence.  
**Issue**: A misconfiguration caused 27 seconds of downtime for 50% of Cloudflare’s traffic.  
**Lesson**: Fast convergence is critical; optimize BGP timers and peerings.  
**Source**: Cloudflare post-mortem.

## Case Study 4: YouTube Hijack (2008)

**Context**: Pakistan Telecom (AS9929) advertised YouTube’s prefix (208.65.153.0/24).  
**Issue**: Global traffic was blackholed, blocking YouTube for hours.  
**Lesson**: BGP lacks inherent security; RPKI and prefix filtering are essential.  
**Source**: Public reports from 2008.

## Case Study 5: Facebook Outage (2021)

**Context**: BGP/OSPF interaction error in Facebook’s backbone.  
**Issue**: BGP withdrew prefixes, and OSPF failed to reroute internally, causing 6-hour downtime.  
**Lesson**: Test protocol interactions; monitor redistribution.  
**Source**: Facebook engineering blog.

## Case Study 6: BGP Security Flaws

**Context**: RPKI adoption is incomplete; software bugs exist.  
**Issue**: Misconfigured RPKI validators rejected valid routes in 2023.  
**Lesson**: Robust testing and redundancy in security mechanisms are needed.  
**Source**: Routing security forums.

These cases highlight real-world challenges, emphasizing the need for robust protocols, security, and monitoring in modern networks.
```
