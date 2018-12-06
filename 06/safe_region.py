from data import coordinates
from time import time
import operator

start_time = time()

min_x = min(coordinates, key=lambda item: item[0])[0]
max_x = max(coordinates, key=lambda item: item[0])[0]
min_y = min(coordinates, key=lambda item: item[1])[1]
max_y = max(coordinates, key=lambda item: item[1])[1]
point_map = [[0 for x in range(min_x, max_x)] for y in range(min_y, max_y)]

# Calculate distances and select closest point for active map points
for map_y, row in enumerate(point_map):
	for map_x, point in enumerate(row):
		# Calculate map point distances to all target points
		point_distances = []
		for target_point in coordinates:
			distance = abs(map_x - (target_point[0] - min_x)) + abs(map_y - (target_point[1] - min_y))
			point_distances.append(distance)

		# Calculate total distance to all target points
		point_map[map_y][map_x] = sum(point_distances)

# Calculate total area with total distance of <10000
safe_area = 0
for row in point_map:
	for total_distance in row:
		if total_distance < 10000:
			safe_area += 1

print('Safe region area is', safe_area)

print('Finished in', time() - start_time)
