import os
import platform
import subprocess
import sys

def install_requirements():
    """Install required packages from requirements.txt"""
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
        [4] Run Ethernet Stress Test
        [5] Exit
        """)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            detect_system()
        elif choice == "2":
            update_script()
        elif choice == "3":
            install_requirements()
        elif choice == "4":
            run_ethernet_stress()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option selected.")
        
        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    display_ui()
