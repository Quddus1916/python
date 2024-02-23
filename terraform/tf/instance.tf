resource "aws_instance" "web_server" {
    ami = "ami-0449c34f967dbf18a"
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.allow_ssh.id]
    associate_public_ip_address = true
    key_name = "vpc_key"
    tags = {
      Name = "Testwebserver"
    }
}
