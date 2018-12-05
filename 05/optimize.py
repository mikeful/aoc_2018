from data import polymer
from time import time
from string import ascii_lowercase
import re

start_time = time()

shortest_polymer = 99999

for char in ascii_lowercase:
	remaining = list(re.sub(char, "", polymer, flags=re.IGNORECASE))
	should_continue = True

	while should_continue:
		last_length = len(remaining)

		# Check and collapse pairs
		for index in range(0, last_length):
			try:
				pair = [remaining[index], remaining[index + 1]]
				if None not in pair:
					if pair[1] in ascii_lowercase and pair[0] == pair[1].upper():
						remaining[index] = None
						remaining[index + 1] = None
					elif pair[0] in ascii_lowercase and pair[0].upper() == pair[1]:
						remaining[index] = None
						remaining[index + 1] = None
			except IndexError:
				pass

		# Filter collapsed/padding value from list
		remaining = [x for x in remaining if x is not None]
		
		# Stop processing if polymer is no longer shortening
		if last_length == len(remaining):
			should_continue = False

	print(char, len(remaining))

	if len(remaining) < shortest_polymer:
		shortest_polymer = len(remaining)

print('Shorest polymer', shortest_polymer)

print('Finished in', time() - start_time)
