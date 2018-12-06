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
		point_distances = {}
		for target_point_id, target_point in enumerate(coordinates):
			distance = abs(map_x - (target_point[0] - min_x)) + abs(map_y - (target_point[1] - min_y))
			point_distances[target_point_id] = distance

		# Get shortest distance and target point index
		shortest_point_id, shortest_distance = min(point_distances.items(), key=operator.itemgetter(1))

		# Check for duplicate shortest distance
		duplicate_distances = 0
		for target_point_id, point_distance in point_distances.items():
			if point_distance == shortest_distance:
				duplicate_distances += 1
		if duplicate_distances < 2:
			point_map[map_y][map_x] = shortest_point_id
		else:
			point_map[map_y][map_x] = None

# Mark areas touching edges as inactive
skip_points = set([None])
for point_id in point_map[0] + point_map[-1]:
	skip_points.add(point_id)
for row in point_map:
	skip_points.add(row[0])
	skip_points.add(row[-1])

# Calculate total area per target point
target_point_areas = {}
for row in point_map:
	for point_id in row:
		if point_id not in skip_points:
			if point_id not in target_point_areas:
				target_point_areas[point_id] = 0
			target_point_areas[point_id] += 1

point_id, largest_area = max(target_point_areas.items(), key=operator.itemgetter(1))
print('Largest point is', point_id, 'with area of', largest_area)

print('Finished in', time() - start_time)
