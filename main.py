import ansible_runner

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

r = ansible_runner.run(private_data_dir='./private', playbook='p2.yml', artifacts_handler=my_artifacts_handler, status_handler=my_status_handler, event_handler=my_event_handler)
print("{}: {}".format(r.status, r.rc))

for each_host_event in r.events:
    print(each_host_event['event'])
print("Final status:")
print(r.stats)