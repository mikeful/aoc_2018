from data import requirements
from time import time
import re

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

todo = set(tasks.keys())
done = []

todo_changed = True
while len(todo) > 0:
	# Search available tasks
	available = set()
	for task in todo:
		if set(tasks[task]).issubset(set(done)):
			available.add(task)

	# Do first task alphabetically
	task_to_do = sorted(list(available))[0]
	done.append(task_to_do)
	todo.remove(task_to_do)

print('Solution', ''.join(done))

print('Finished in', time() - start_time)
