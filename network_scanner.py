import scapy.all as scapy
import optparse

def get_user_input():
	parse_object = optparse.OptionParser()
	parse_object.add_option('-i','--ipaddress',dest='ipaddress',help='get ip address')

	(user_input,arguments) = parse_object.parse_args()

	if not user_input.ipaddress:
		print('input ip address: ')
	return user_input

def scan_network(ip):
	arp_request_packet = scapy.ARP(pdst=ip)
	broadcast_request = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	combined_packet = broadcast_request/arp_request_packet

	(answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)

	answered_list.summary()
user_ip_address = get_user_input()
scan_network(user_ip_address.ipaddress)
