from time import time
from functools import lru_cache
from itertools import product
from random import randint

serial_number = 1788

@lru_cache(maxsize=90000)
def calculate_power(x, y):
	rack_id = x + 10
	power_level = ((rack_id * y) + serial_number) * rack_id
	try:
		power_level = int((list(str(power_level))[::-1])[2])
	except IndexError as e:
		power_level = 0
	return power_level - 5

def calculate_area(coordinates):
	if coordinates[0] + coordinates[2] > 300 or coordinates[1] + coordinates[2] > 300:
		return -999999
	levels = []
	for x, y in product(range(0, coordinates[2]), repeat=2):
		levels.append(calculate_power(coordinates[0] + x, coordinates[1] + y))
	return sum(levels)

if __name__ == '__main__':
	start_time = time()

	largest_level = -99999
	largest_solution = [randint(1,300), randint(1,300), randint(1,300)]
	level = -99999
	current_solution = [randint(1,300), randint(1,300), randint(1,300)]
	change_counter = 0
	reset_counter = 0
	solution_time = time()

	while level < 1000:
		change_counter += 1

		# Swap two tasks in solution and evaluate it
		new_x = current_solution[0] + randint(-15, 15)
		new_y = current_solution[1] + randint(-15, 15)
		new_size = current_solution[2] + randint(-15, 15)
		if new_x < 1:
			new_x = 1
		if new_x > 300:
			new_x = 300
		if new_y < 1:
			new_y = 1
		if new_y > 300:
			new_y = 300
		if new_size < 1:
			new_size = 1
		if new_size > 300:
			new_size = 300

		current_solution = [new_x, new_y, new_size]
		level = calculate_area(current_solution)

		# Check if better solution was found
		if level > largest_level:
			largest_solution = current_solution.copy()
			largest_level = level
			change_counter = 0
			reset_counter = 0
			solution_time = time()

		# Reset current solution to last good solution after too many tries
		if change_counter > 3000:
			change_counter = 0
			reset_counter += 1
			current_solution = largest_solution.copy()

		# Retry from start if solving takes too long
		if time() - solution_time > 30:
			print(largest_solution, largest_level)
			largest_level = -99999
			largest_solution = [randint(1,300), randint(1,300), randint(1,300)]
			change_counter = 0
			reset_counter = 0
			solution_time = time()
			current_solution = [randint(1,300), randint(1,300), randint(1,300)]

	print('Finished in', time() - start_time)
