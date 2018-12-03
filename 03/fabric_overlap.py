from data import parts
from time import time

start_time = time()

max_width = 1000
max_height = 1000
overlap_counts = [[0 for x in range(max_width)] for y in range(max_height)]

# Fill overlaps
for part in parts:
	pos_x = part['pos'][0]
	pos_y = part['pos'][1]
	width = part['size'][0]
	height = part['size'][1]

	for part_y in range(pos_y, pos_y + height):
		for part_x in range(pos_x, pos_x + width):
			overlap_counts[part_y][part_x] += 1

# Scan for overlapping squares
overlap_counter = 0
for row in overlap_counts:
	overlap_counter += sum(1 for x in row if x > 1)

print('Overlapping square inches:', overlap_counter)
print('Finished in', time() - start_time)
