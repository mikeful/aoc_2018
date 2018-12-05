from data import polymer
from time import time
from string import ascii_lowercase
import re

start_time = time()

# Generate regex patters for valid to remove
remove_patters = []
for char in ascii_lowercase:
	remove_patters.append(re.compile(char + char.upper()))
	remove_patters.append(re.compile(char.upper() + char))

remaining = polymer
should_continue = True

while should_continue:
	last_length = len(remaining)

	# Collapse pairs
	for pattern in remove_patters:
		remaining = pattern.sub("", remaining)
	
	# Stop processing if polymer is no longer shortening
	if last_length == len(remaining):
		should_continue = False

print(''.join(list(remaining)))
print(len(remaining))

print('Finished in', time() - start_time)
