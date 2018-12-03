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

# Scan for single non overlapping part
for part in parts:
	part_id = part['id']
	pos_x = part['pos'][0]
	pos_y = part['pos'][1]
	width = part['size'][0]
	height = part['size'][1]

	overlap_counter = 0
	for row in overlap_counts[pos_y:pos_y + height]:
		overlap_counter += sum(1 for x in row[pos_x:pos_x + width] if x > 1)

	if overlap_counter == 0:
		break

print('Non overlapping id:', part_id)
print('Finished in', time() - start_time)
