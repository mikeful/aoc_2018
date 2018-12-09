from data import requirements
from time import time
import re
import random
from functools import lru_cache

start_time = time()

req_pattern = re.compile('Step (?P<dependency>.).* step (?P<step>.)')
tasks = {}

# Extract tasks and dependecies
for requirement in requirements:
	parsed = req_pattern.search(requirement).groupdict()
	task = parsed['step']
	task_dep = parsed['dependency']
	if task not in tasks:
		tasks[task] = []
	tasks[task].append(task_dep)

# Sort dependencies
tasks = {task_deps:sorted(tasks[task_deps]) for task_deps in tasks.keys()}

@lru_cache(maxsize=20000)
def check_rules(task_string):
	penalty_score = 0
	for slice_start in range(len(task_string) - 1):
		task = task_string[slice_start]
		task_slice = task_string[(slice_start + 1):]
		for check_dep in tasks[task]:
			if check_dep in task_slice:
				penalty_score += 1
	return penalty_score

smallest_penalty = 99999
smallest_solution = []
penalty = 9999
task_solution = list(tasks.keys())
swap_counter = 0
reset_counter = 0
solution_time = time()

# Find valid solution with random guided search
while penalty > 0:
	swap_counter += 1

	# Swap two tasks in solution and evaluate it
	a = random.randint(0, len(task_solution) - 1)
	b = random.randint(0, len(task_solution) - 1)
	while b == a:
		b = random.randint(0, len(task_solution) - 1)
	task_solution[b], task_solution[a] = task_solution[a], task_solution[b]
	penalty = check_rules(''.join(task_solution))

	# Check if better solution was found
	if penalty < smallest_penalty:
		smallest_solution = task_solution.copy()
		smallest_penalty = penalty
		swap_counter = 0
		reset_counter = 0
		solution_time = time()

	# Reset current solution to last good solution after too many tries
	if swap_counter > len(task_solution) + smallest_penalty * 10:
		swap_counter = 0
		reset_counter += 1
		task_solution = smallest_solution.copy()

	# Retryn from start if solving takes too long
	if time() - solution_time > 5:
		smallest_penalty = 99999
		smallest_solution = []
		swap_counter = 0
		reset_counter = 0
		solution_time = time()
		random.shuffle(task_solution)

print('Valid solution found:', ''.join(task_solution))

solution_changed = True
while solution_changed:
	for index, task in enumerate(task_solution[:-1]):
		solution_changed = False
		if ord(task) > ord(task_solution[index + 1]):
			task_solution[index], task_solution[index + 1] = task_solution[index + 1], task_solution[index]
			penalty = check_rules(''.join(task_solution))
			if penalty > 0:
				task_solution[index], task_solution[index + 1] = task_solution[index + 1], task_solution[index]
			else:
				solution_changed = True

print('Solution after sort:', ''.join(task_solution))

print('Finished in', time() - start_time)
