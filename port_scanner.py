"""
PORT SCANNER APPLICATION
========================

Description:
This is a simple port scanner tool that scans a target website/IP address 
to identify open ports within the range of 20-1024 (common ports).

How it works:
1. Takes a website or IP address as input from the user
2. Iterates through ports 20 to 1024
3. Attempts to establish a TCP connection on each port
4. Reports which ports are OPEN (accepting connections)
5. Uses a timeout of 0.5 seconds to speed up the scanning process

Usage:
------
Run the script: python port_scanner.py
Enter the target when prompted (e.g., google.com, 192.168.1.1)
Wait for the scan to complete

Features:
---------
- Simple and easy to use
- Scans common ports (20-1024)
- Fast scanning with timeout optimization
- Clear output showing open ports

Requirements:
---------
- Python 3.x
- socket module (built-in)

Example Output:
---------
Enter website (example: google.com): google.com
Scanning target: google.com
Port 80 is OPEN
Port 443 is OPEN

Note: This tool is for educational purposes. Always get permission before 
scanning networks or systems you don't own.
"""

import socket

target = input("Enter website (example: google.com): ")

print("Scanning target:", target)

for port in range(20, 1025):  # common ports
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    
    s.close()
