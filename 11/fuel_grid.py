from time import time
from functools import lru_cache
from itertools import product
from multiprocessing import Pool

serial_number = 1788

@lru_cache(maxsize=5000)
def calculate_power(x, y):
	rack_id = x + 10
	power_level = ((rack_id * y) + serial_number) * rack_id
	try:
		power_level = int((list(str(power_level))[::-1])[2])
	except IndexError as e:
		power_level = 0
	return power_level - 5

def calculate_area(coordinates):
	levels = []
	for x, y in product(range(0, 3), repeat=2):
		levels.append(calculate_power(coordinates[0] + x, coordinates[1] + y))
	return sum(levels)

if __name__ == '__main__':
	start_time = time()

	# Calculate list of power levels
	process_pool = Pool(None)
	coordinates = list(product(range(1, 299), repeat=2))
	coordinate_levels = process_pool.map(calculate_area, coordinates)

	# Get largest power level and get coordinates for it
	largest_level = max(coordinate_levels)
	larget_index = coordinate_levels.index(largest_level)
	larget_coordinates = list(coordinates)[larget_index]

	print(larget_coordinates)

	print('Finished in', time() - start_time)
