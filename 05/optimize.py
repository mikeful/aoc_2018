from data import polymer
from time import time
from multiprocessing import Pool
from string import ascii_lowercase
import re

start_time = time()

# Generate regex patters for valid to remove
remove_patters = []
for char in ascii_lowercase:
	remove_patters.append(re.compile(char + char.upper()))
	remove_patters.append(re.compile(char.upper() + char))

def collapse(remaining):
	should_continue = True

	while should_continue:
		last_length = len(remaining)

		# Collapse pairs
		for pattern in remove_patters:
			remaining = pattern.sub("", remaining)
		
		# Stop processing if polymer is no longer shortening
		if last_length == len(remaining):
			should_continue = False

	return len(remaining)

# Generate all variations of polymer
variations = []
for char in ascii_lowercase:
	variations.append(re.sub(char, "", polymer, flags=re.IGNORECASE))

if __name__ == '__main__':
	# Collapse variations in multiple "threads"
	process_pool = Pool(None)
	collapsed_lengths = process_pool.map(collapse, variations)

	shortest_polymer = len(polymer)
	for result in collapsed_lengths:
		if result < shortest_polymer:
			shortest_polymer = result

	print('Shorest polymer', shortest_polymer)

	print('Finished in', time() - start_time)
