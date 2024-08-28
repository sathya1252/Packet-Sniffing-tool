Packet Sniffing Tool

This project is a lightweight packet sniffing tool built using Python and the Scapy library. It allows users to monitor and capture network packets in real-time on a specified network interface. The tool can be customized with various filters to target specific types of network traffic, such as TCP, UDP, ICMP, or traffic on specific ports.

Features:
 
-> Real-Time Packet Capture: Capture and analyze network packets on a specified interface.

-> Customizable Filters: Apply filters to capture only the traffic you're interested in, using BPF (Berkeley Packet Filter) syntax.

-> Simple and Extensible: Easy to modify and extend for more complex network analysis tasks.

-> Cross-Platform: Runs on both Linux and Windows, with support for Npcap on Windows.


Requirements:

    Python 3.x
    Scapy
    Npcap (for Windows)

Usage:

Clone the repository:

    git clone https://github.com/sathya1252/packet-sniffing-tool.git

Make sure you have Python3 installed.

    cd packet-sniffing-tool

Install the required dependencies:

    pip install -r requirements.txt

Run the script with administrative privileges:

    sudo python3 main.py

Customize the network interface and filters within the script to meet your needs.
