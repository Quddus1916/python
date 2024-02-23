import ansible_runner
import json

# i = ansible_runner.get_inventory(action='list', inventories=['./ansible_liabrary/hosts'])
# print(i)

# Retrieve the inventory information
i = ansible_runner.get_inventory(action='host', inventories=['./ansible_liabrary/hosts'], host='host2')
print("*******")
i_dict = json.loads(i[0])
val = i_dict['ansible_host']
print(val)


# Now 'host_info_dict' contains the dictionary

# i = ansible_runner.get_inventory(action='graph', inventories=['./ansible_liabrary/hosts'])
# print(i)