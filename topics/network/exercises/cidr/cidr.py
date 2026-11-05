"""IPv4 CIDR и longest-prefix match. Только вычисления, без сетевых запросов."""
import argparse
from ipaddress import IPv4Address, IPv4Network
import json


def describe(cidr):
    if not isinstance(cidr, str) or '/' not in cidr:
        raise ValueError('Нужна строка IPv4 CIDR с явным префиксом')
    network = IPv4Network(cidr, strict=True)
    reserve = 1 if network.prefixlen < 31 else 0
    return {'network': str(network), 'netmask': str(network.netmask),
            'address_count': network.num_addresses,
            'host_count': network.num_addresses - 2 * reserve,
            'first_host': str(network.network_address + reserve),
            'last_host': str(network.broadcast_address - reserve),
            'last_address': str(network.broadcast_address),
            'has_conventional_broadcast': network.prefixlen < 31}


def route_for(destination, routes):
    destination = IPv4Address(destination)
    matches = [IPv4Network(route, strict=True) for route in routes]
    matches = [route for route in matches if destination in route]
    return str(max(matches, key=lambda route: route.prefixlen)) if matches else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cidr')
    args = parser.parse_args()
    try:
        result = describe(args.cidr)
    except (ValueError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
