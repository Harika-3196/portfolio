create an virtual env

To install venv: python3 -m venv ./venv
To activate venv: source ./venv/bin/activate
To deactivate venv: deactivate


export FLASK_APP=server.py

flask run --host=0.0.0.0

# Installing Ngnix on Ec2 Machine
sudo amazon-linux-extras install nginx1
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx