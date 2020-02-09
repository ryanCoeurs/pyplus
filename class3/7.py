"""
7. You have the following BGP configuration from a Cisco IOS-XR router: 

router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this. 

BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]

"""
from ciscoconfparse import CiscoConfParse

config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

config = CiscoConfParse(config.splitlines())


bgp_neighbors = config.find_objects_w_parents(parentspec=r"^router bgp", childspec=r"^\s+neighbor")
bgp_peers = []
for neighbor in bgp_neighbors:
    neighbor_ip = neighbor.text.split()[1]
    for line in neighbor.children:
        if "remote-as" in line.text:
            neighbor_as = line.text.split()[1]
            bgp_peers.append((neighbor_ip, neighbor_as))

print("BGP Peers:")
print(bgp_peers)

