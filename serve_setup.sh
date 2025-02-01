#!/bin/bash
export HOME=/home/ec2-user
sudo yum update
sudo yum install ec2-instance-connect
sudo yum install stress-ng -y
sudo yum install htop -y
sudo yum install python3-pip -y
sudo python3 -m pip install flask
sudo python3 -m pip install subprocess.run
sudo python3 -m pip install sockets
sudo yum install git -y
cd /home/ec2-user
git clone REDACTEDFORPRIVACY
cd /home/ec2-user/CCA-MP2
python3 serve.py & 