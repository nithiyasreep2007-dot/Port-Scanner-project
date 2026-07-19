import socket

def start_sniffer():
    try:
        # Create raw socket
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

        print("Sniffer started... Listening for packets 👀")

        while True:
            raw_data, addr = sniffer.recvfrom(65535)

            print("\nPacket Received!")
            print(f"From IP: {addr[0]}")

    except PermissionError:
        print("Run this program as Administrator / Root ⚠️")

# Run program
start_sniffer()