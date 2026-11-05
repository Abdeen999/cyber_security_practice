import socket

# Target IP address (Localhost / Loopback address)

target_host = "127.0.0.1"
target_port = 80

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

print(f"Checking connection to {target_host} on port {target_port}...")

# Try connecting to the target
result = soc

k.connect_ex((target_host, target_port))

if result == 0:
    print(f"Port {target_port} is OPEN!")
else:
    print(f"Port {target_port} is CLOSED or filtered.")

sock.close()