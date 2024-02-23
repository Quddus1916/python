from python_terraform import *
t = Terraform( working_dir= './tf')
return_code, stdout, stderr = t.apply(skip_plan=True, target='aws_security_group.allow_ssh')
print("****")
print(return_code)
print(stdout)
print(stderr)