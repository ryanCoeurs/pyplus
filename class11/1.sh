curl -s https://netbox.lasthop.io/api/ --insecure


curl -s https://netbox.lasthop.io/api/ --insecure | jq


curl -H "Authorization: Token $NETBOX_TOKEN" https://netbox.lasthop.io/api/dcim/devices/ --insecure | jq


curl -H "Authorization: Token $NETBOX_TOKEN" https://netbox.lasthop.io/api/dcim/devices/2/ --insecure | jq
