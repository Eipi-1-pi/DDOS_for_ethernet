import os
import platform
import subprocess
import sys

def install_requirements():
    """Install required packages from requirements.txt"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def update_script():
    """Pull the latest changes from the repository"""
    subprocess.check_call(["git", "pull"])

def detect_system():
    """Detect the operating system"""
    system = platform.system()
    if system == "Linux":
        print("System detected: Linux")
    elif system == "Windows":
        print("System detected: Windows")
    elif system == "Darwin":
        print("System detected: macOS")
    else:
        print("System detected: Unknown")

def run_ethernet_stress():
    """Run the Ethernet_stress(wifi).py script"""
    subprocess.check_call([sys.executable, "Ethernet_stress(wifi).py"])

def display_ui():
    """Display the UI with options"""
    print("""
     ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗ █████╗ ███╗   ██╗████████╗
     █████╗ ████║██║   ██║██╔════╝██║██╔════╝██╔══██╗████╗  ██║╚══██╔══╝
     ██╔████╔██║██║   ██║█████╗  ██║██║     ███████║██╔██╗ ██║   ██║   
     ██║╚██╔╝██║██║   ██║██╔══╝  ██║██║     ██╔══██║██║╚██╗██║   ██║   
     ██║ ╚═╝ ██║╚██████╔╝██║     ██║╚██████╗██║  ██║██║ ╚████║   ██║   
     ╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   

    [1] Detect System
    [2] Update Script
    [3] Install Requirements
    [4] Run Ethernet Stress Test
    """)

if __name__ == "__main__":
    display_ui()
    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        detect_system()
    elif choice == "2":
        update_script()
    elif choice == "3":
        install_requirements()
    elif choice == "4":
        run_ethernet_stress()
    else:
        print("Invalid option selected.")
