import socket

target = "127.0.0.1"

print(f"[*] Day 3 Advanced Scan on: {target}")
for port in range(1,  51):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.3)
	result = s.connect_ex((target, port))
	if result == 0:
		print(f"[+] port {port} is OPEN")
	s.close()
print("[*] Day 3 Scan completed!")
