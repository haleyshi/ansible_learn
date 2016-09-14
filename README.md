# ansible_learn

# Prepare for the environment
-----------------------------
$ vagrant init
$ vi Vagrantfile
$ vagrant up

$ vagrant ssh acs
acs $ sudo apt-add-repository ppa:ansible/ansible
acs $ sudo apt-get update
acs $ sudo apt-get install ansible
acs $ ansible --version
