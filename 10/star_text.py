from data import stars
from time import time
from copy import deepcopy

start_time = time()

# Simulate star movement
counter = 0
min_x = 9999
max_x = 0
min_y = 9999
max_y = 0
bounding_height = 999999999998
last_box_height = 999999999999
last_stars = stars.copy()

while bounding_height < last_box_height:
	last_box_height = bounding_height
	if bounding_height < 100:
		last_stars = deepcopy(stars)
	for star in stars:
		star['position'][0] += star['velocity'][0]
		star['position'][1] += star['velocity'][1]
	min_x = min([star['position'][0] for star in stars])
	max_x = max([star['position'][0] for star in stars])
	min_y = min([star['position'][1] for star in stars])
	max_y = max([star['position'][1] for star in stars])
	bounding_height = abs(max_x - min_x)
	counter += 1

# Extract star status to 2d array
star_map = [[0 for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
for star in last_stars:
	star_map[star['position'][1] - min_y][star['position'][0] - min_x] = 1

# Display text made of stars
for map_y, row in enumerate(star_map):
	row_string = ''
	for map_x, space in enumerate(row):
		row_string += '.' if not space else '#'
	print(row_string)

print('Simulated for', (counter - 1), 'seconds')

print('Finished in', time() - start_time)