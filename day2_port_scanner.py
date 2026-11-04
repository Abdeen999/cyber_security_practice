import socket

target = "127.0.0.1"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
result = s.connect_ex((target, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")
s.close()