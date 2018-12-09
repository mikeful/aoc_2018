from data import requirements
from time import time
import re

def get_task_duration(task_id):
	return 60 + (ord(task_id) - 64)

start_time = time()

req_pattern = re.compile('Step (?P<dependency>.).* step (?P<step>.)')
tasks = {}

# Extract tasks and dependecies
for requirement in requirements:
	parsed = req_pattern.search(requirement).groupdict()
	task = parsed['step']
	task_dep = parsed['dependency']
	if task not in tasks:
		tasks[task] = set()
	for dep_task in task_dep:
		if dep_task not in tasks:
			tasks[dep_task] = set()
	tasks[task].add(task_dep)

# Simulate multiple workers with time counters and tasks moved out of queue
worker_times = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
worker_tasks = {0: '', 1: '', 2: '', 3: '', 4: ''}
todo = set(tasks.keys())
done = []
seconds_counter = 0
while len(done) < len(tasks):
	seconds_counter += 1
	for worker_id, worker_task in worker_tasks.items():
		if worker_tasks[worker_id] != '':
			# Work work work
			worker_times[worker_id] -= 1
			if worker_times[worker_id] <= 0:
				done.append(worker_task)
				worker_tasks[worker_id] = ''
		if worker_tasks[worker_id] == '':
			# Search available tasks
			available = set()
			for task in todo:
				if set(tasks[task]).issubset(set(done)):
					available.add(task)

			if len(available) > 0:
				# Do first task alphabetically
				task_to_do = sorted(list(available))[0]
				todo.remove(task_to_do)
				worker_tasks[worker_id] = task_to_do
				worker_times[worker_id] = get_task_duration(task_to_do)
	print(seconds_counter, worker_tasks)

print('Solution', seconds_counter - 1)

print('Finished in', time() - start_time)
