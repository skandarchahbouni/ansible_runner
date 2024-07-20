import ansible_runner
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

def my_artifacts_handler(artifacts_dir):
    # Do something here
    pass
    # print(artifacts_dir)

def my_status_handler(data, runner_config):
    # Do something here
    pass

def my_event_handler(data):
    # Do something here
    pass




if __name__ == "__main__":
    # hosts = [
    #     {'alias': 'host1', 'host': '192.168.1.1', 'user': 'user1', 'group': 'group1'},
    #     {'alias': 'host2', 'host': '192.168.1.2', 'user': 'user2'},
    #     {'alias': 'host3', 'host': '192.168.1.3', 'group': 'group2'},
    #     {'alias': 'host4', 'host': '192.168.1.4'}
    # ]
    hosts = [
        {'alias': 'host1', 'host': '13.83.121.162', 'user': 'azureuser'}
    ]
    file_path = './private/inventory/inventory.yml'
    print("generating inventory ....")
    generate_ansible_inventory(hosts, file_path)

    print("running ansible playbook ...")
    r = ansible_runner.run(private_data_dir='./private', playbook='p1.yml', artifacts_handler=my_artifacts_handler, status_handler=my_status_handler, event_handler=my_event_handler)
    print("{}: {}".format(r.status, r.rc))
    for each_host_event in r.events:
        print(each_host_event['event'])
    print("Final status:")
    print(r.stats)





