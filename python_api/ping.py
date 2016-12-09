import json
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor

loader = DataLoader()
variable_manager = VariableManager()
inventory = Inventory(loader=loader, variable_manager=variable_manager)
variable_manager.set_inventory(inventory)

class Options(object):
	def __init__(self):
		self.connection = "local"
		self.forks = 10
		self.check = False

	def __getattr__(self, name):
		return None

options = Options()

def run_adhoc():
	variable_manager.extra_vars={"ansible_ssh_user":"root" , "ansible_ssh_pass":"r00tme"}
	play_source = {"name":"Ansible Ad-Hoc","hosts":"10.20.0.3","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"w"}}]}
	play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
	tqm = None
    	try:
        	tqm = TaskQueueManager(
            		inventory=inventory,
            		variable_manager=variable_manager,
            		loader=loader,
            		options=options,
            		passwords=None,
            		#stdout_callback='minimal',
            		run_tree=False,
        		)
        	result = tqm.run(play)
        	print result
    	finally:
        	if tqm is not None:
            		tqm.cleanup()

def run_playbook(playbooks):
	variable_manager.extra_vars={"ansible_ssh_user":"root" , "ansible_ssh_pass":"r00tme"} 
    	pb = PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=None)
    	result = pb.run()
    	print result


if __name__ == '__main__':
	run_adhoc()
	#run_playbook(['ping.yml'])
