# Vagrant virtual development env

This is only the skeleton of the virtual development environment.
For the actual application, please see [here](https://github.com/haoguanqing/Tinyurl).


*Some tutorial for beginners*
```
vagrant up
vagrant ssh

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
sudo apt-get install python-dev
sudo apt-get install postgresql postgresql-contrib

cd /vagrant
sudo python get-pip.py
git clone https://github.com/haoguanqing/Tinyurl.git

cd Tinyurl
sudo pip install -r requirements.txt
```
