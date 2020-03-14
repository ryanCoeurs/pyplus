"""
3. Using your external YAML file and your function located in my_funcs.py, use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". From this routing table data, extract all of the static and connected routes from the default VRF. Print these routes to the screen and indicate whether the route is a connected route or a static route. In the case of a static route, print the next hop address.
"""

import pyeapi
from my_funcs import get_inventory, print_table
from pprint import pprint

inventory = get_inventory()

for device, device_dict in inventory.items():
    connection = pyeapi.client.connect(**device_dict)
    device_api = pyeapi.client.Node(connection)
    route_table = device_api.run_commands("show ip route")
    route_table = route_table[0]

    #VRFs
    vrfs = route_table['vrfs']
    for vrf, vrf_table in vrfs.items(): 
        #routes
        routes = vrf_table['routes']
        for route, route_details in routes.items():
            route_indicator = "C"
            next_hop = ""
            if route_details['routeType'] == 'static':
                route_indicator = "S"
                vias = route_details['vias'][0]
                next_hop = vias['nexthopAddr']
            print(f"{route_indicator}  {route}  {next_hop}")
    
