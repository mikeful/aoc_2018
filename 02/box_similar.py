from multiprocessing import Pool
from itertools import combinations
from time import time
from data import box_ids

def compare_ids(ids):
	id1 = ids[0]
	id2 = ids[1]
	differences = 0
	return_string = ''

	for index, char1 in enumerate(list(id1)):
		char2 = id2[index]

		if char1 == char2:
			return_string += char1
		else:
			differences += 1

		if differences > 1:
			return

	return return_string

if __name__ == '__main__':
	start_time = time()

	box_ids.sort()

	process_pool = Pool(4)
	comparisons = process_pool.map(compare_ids, combinations(box_ids, 2))

	for result in comparisons:
		if result:
			print(result)

	print('Finished in', time() - start_time)
