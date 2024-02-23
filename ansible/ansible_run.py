import ansible_runner
import yaml
m = "value"
 

with open(r'./playbook/var.yml') as f:
    doc = yaml.full_load(f)

doc['messg']= "default"
doc['host']=  "host2"

with open('./playbook/var.yml', 'w') as f:
    yaml.dump(doc, f)


r = ansible_runner.run(playbook='./playbook/simple_playbook.yml',private_data_dir='.',inventory = 'hosts',)
# successful: 0
print("Final status:")
print(r.stats)