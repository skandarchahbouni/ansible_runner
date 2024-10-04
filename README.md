# Ansible Inventory Generator & Playbook Runner ⚙️🚀

This project provides a simple script for generating an Ansible inventory file and running an Ansible playbook. It uses the `ansible_runner` library to automate the deployment process on specified hosts.

## Features

- Generates an Ansible inventory in YAML format.
- Executes a specified Ansible playbook on the defined hosts.
- Supports optional parameters like user and group for hosts.

## Prerequisites

- Python 3.x
- Ansible
- `ansible_runner` library

## Installation

1. Install Ansible:

   ```bash
   sudo apt update
   sudo apt install ansible
   ```

2. Install `ansible_runner`:

   ```bash
   pip install ansible-runner
   ```

## Usage

1. Define your hosts in the script:
   ```python
   hosts = [
       {'alias': 'host1', 'host': 'your_host_ip', 'user': 'your_user'}
   ]
   ```

2. Specify the path for the inventory file:
   ```python
   file_path = './path/to/your/inventory.yml'
   ```

3. Run the script:
   ```bash
   python your_script_name.py
   ```

4. The script will generate an inventory file and run the specified Ansible playbook (`p1.yml`).

## Example

To see how to define hosts and customize the inventory, check the comments in the script.
