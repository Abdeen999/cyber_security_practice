import requests

def simple_recon():
    target_url = input("Enter a website URL (e.g., https://google.com): ")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        print(f"\n[*] Starting reconnaissance on: {target_url}")
        response = requests.get(target_url, headers=headers, timeout=5)
        
        print(f"[+] HTTP Status Code: {response.status_code}")
        if response.status_code == 200:
            print("    Analysis: Target is active and accessible.")
        else:
            print("    Analysis: Potential restriction or issue.")
            
        print("\n" + "="*30 + " [ HTTP HEADERS ] " + "="*30)
        server_info = response.headers.get('Server', 'Not disclosed')
        print(f"[!] Server Software/OS identified: {server_info}")
        
        print("\n[+] Full Headers Dump:")
        for header, value in response.headers.items():
            print(f"    {header}: {value}")
            
    except requests.exceptions.MissingSchema:
        print("[-] Error: URL must start with http:// or https://")
    except requests.exceptions.ConnectionError:
        print("[-] Error: Could not connect to the target website.")
    except requests.exceptions.Timeout:
        print("[-] Error: Connection attempt timed out.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
    simple_recon()

