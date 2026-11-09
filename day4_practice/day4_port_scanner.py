import socket

target = input("Enter Target IP: ")
start_port = int(input("Enter Start port: "))
end_port = int(input("Enter End port: "))

print(f"[*] Starting Day 4 scan on: {target}")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] port {port} is open")
        
    s.close()