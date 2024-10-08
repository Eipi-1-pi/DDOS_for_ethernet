import os
import platform
import subprocess
import sys

def install_system_dependencies():
    """Install system-level dependencies"""
    try:
        if platform.system() == "Linux":
            subprocess.check_call(["sudo", "apt", "update"])
            subprocess.check_call(["sudo", "apt", "install", "-y", "hping3", "asyncrone", "ufonet", "goldeneye", "routersploit", "websploit", "commix", "web2attack"])
        elif platform.system() == "Darwin":  # macOS
            subprocess.check_call(["brew", "install", "hping3", "asyncrone", "ufonet", "goldeneye", "routersploit", "websploit", "commix"])
        else:
            print("Unsupported system for automated system-level dependency installation. Please install manually.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install system-level dependencies: {e}")

def install_requirements():
    """Install required Python packages from requirements.txt"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")

def update_script():
    """Pull the latest changes from the repository"""
    try:
        subprocess.check_call(["git", "pull"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to update script: {e}")

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
    try:
        subprocess.check_call([sys.executable, "Ethernet_stress(wifi).py"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Ethernet stress test: {e}")

def display_ui():
    """Display the UI with options"""
    while True:
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
        [4] Install System Dependencies
        [5] Run Ethernet Stress Test
        [6] Exit
        """)

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            detect_system()
        elif choice == "2":
            update_script()
        elif choice == "3":
            install_requirements()
        elif choice == "4":
            install_system_dependencies()
        elif choice == "5":
            run_ethernet_stress()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option selected.")
        
        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    display_ui()
