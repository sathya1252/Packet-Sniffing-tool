from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def start_sniffing(interface, filter_exp):
    sniff(iface=interface, filter=filter_exp, prn=packet_callback, store=0)

if __name__ == "__main__":
    print("Available interfaces:", get_if_list())
    interface = "Your_Interface_Name_Here"
    # Example filters:
    # "tcp" - Capture only TCP packets
    # "udp" - Capture only UDP packets
    # "icmp" - Capture only ICMP packets
    # "port 80" - Capture packets on port 80 (HTTP)
    # "src host 192.168.1.1" - Capture packets from a specific source IP
    filter_exp = "tcp and port 80"  # Replace with your desired filter
    start_sniffing(interface, filter_exp)
