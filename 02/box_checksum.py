import string
from multiprocessing import Pool
from time import time
from data import box_ids

def count_letters(text):
	two_letters = 0
	three_letters = 0

	for char in string.ascii_lowercase:
		char_count = text.count(char)

		if char_count == 2:
			two_letters = 1
		if char_count == 3:
			three_letters = 1

	return two_letters, three_letters

if __name__ == '__main__':
	start_time = time()

	process_pool = Pool(4)
	letter_counts = process_pool.map(count_letters, box_ids)

	two_letters = 0
	three_letters = 0
	for counts in letter_counts:
		two_letters += counts[0]
		three_letters += counts[1]

	print(two_letters * three_letters)
	print('Finished in', time() - start_time)
