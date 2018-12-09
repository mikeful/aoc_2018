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

# Move task forward in timeline slots until there is no depending task in same slot
task_timeline = [set(tasks), set()]
timeline_changed = True
while timeline_changed:
	timeline_changed = False
	# Check all tasks
	for task, task_deps in tasks.items():
		# Check all slots in timeline
		for slot_index, slot_tasks in enumerate(task_timeline):
			# If task is found in slot
			if task in slot_tasks:
				# Check if there is dependencies in front of or in same slot as current task
				for check_slot_index, check_slot in enumerate(task_timeline[slot_index:]):
					for check_task in check_slot:
						if check_task in task_deps:
							# Depending task found, move current task forward
							try:
								slot_exists = task_timeline[slot_index + 1]
							except IndexError as e:
								task_timeline.append(set())
							task_timeline[slot_index + 1].add(task)
							task_timeline[slot_index].remove(task)
							timeline_changed = True
							print(task_timeline)

							# Stop processing
							break
					if timeline_changed:
						# Task was moved, stop processing comparison timeslots
						break
			if timeline_changed:
				# Task was moved, stop processing main timeslots
				break

# Extract timeline slot data into string ordered alphabetically per slot
task_string = ''
for slot in task_timeline:
 	task_string += ''.join(sorted(list(slot)))

print('Valid solution found:', task_string)

print('Finished in', time() - start_time)
