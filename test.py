import yaml

def generate_ansible_inventory(hosts, file_path):
    inventory = {'all': {'hosts': {}, 'children': {}}}

    # Populate hosts and groups
    for host in hosts:
        alias = host['alias']
        inventory['all']['hosts'][alias] = {'ansible_host': host['host']}
        if 'user' in host:
            inventory['all']['hosts'][alias]['ansible_user'] = host['user']
        if 'group' in host:
            group = host['group']
            if group not in inventory['all']['children']:
                inventory['all']['children'][group] = {'hosts': {}}
            inventory['all']['children'][group]['hosts'][alias] = None

    # Save the inventory to a file
    with open(file_path, 'w') as file:
        yaml.dump(inventory, file, default_flow_style=False)

# Example usage:
hosts = [
    {'alias': 'host1', 'host': '192.168.1.1', 'user': 'user1', 'group': 'group1'},
    {'alias': 'host2', 'host': '192.168.1.2', 'user': 'user2'},
    {'alias': 'host3', 'host': '192.168.1.3', 'group': 'group2'},
    {'alias': 'host4', 'host': '192.168.1.4'}
]

file_path = './private/inventory/inventory.yml'
generate_ansible_inventory(hosts, file_path)
