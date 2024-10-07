# DDOS_for_ethernet-

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [License](#license)

## Introduction
This repository contains a script for performing network stress testing using both Ethernet-based desktop connections and specific IP addresses. The script generates a high volume of traffic to specified URLs, simulating Distributed Denial of Service (DDoS) attacks for testing purposes.

## Features
- Multi-threaded network stress testing
- Supports both Ethernet-based desktop and IP-specific methods
- Randomized user-agent strings for requests
- Asynchronous HTTP requests using `aiohttp`
- Command-line interface for easy configuration

## Prerequisites
- Python 3.6+
- `aiohttp` library

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Eipi-1-pi/DDOS_for_ethernet-.git
    cd DDOS_for_ethernet-
    ```
2. Install the required dependencies:
    ```bash
    pip install aiohttp
    ```

## Usage
1. Run the script:
    ```bash
    python Ethernet_stress(wifi).py
    ```
2. Follow the on-screen instructions to choose the method (Ethernet-based or IP-specific) and enter the required details.

### Example Commands
- To use Ethernet-based desktop:
    ```bash
    python Ethernet_stress(wifi).py
    ```
    Select option `[1]` from the menu.
- To use a specific IP address:
    ```bash
    python Ethernet_stress(wifi).py
    ```
    Select option `[2]` from the menu and enter the IP address when prompted.

## Disclaimer
This script is intended for educational and testing purposes only. The author and contributors are not responsible for any misuse or damage caused by this script. Use it responsibly and only on networks and systems you own or have permission to test.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
