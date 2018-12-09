from data import document
from time import time

def parse_child(unprocessed_part, level=1):
	meta_sum = 0
	child_nodes = unprocessed_part.pop(0)
	meta_fields = unprocessed_part.pop(0)

	# Process children recursively if found in node
	for x in range(child_nodes):
		sub_meta_sum, unprocessed_part = parse_child(unprocessed_part, level+1)
		meta_sum += sub_meta_sum

	# All child nodes handled, process meta fields		
	for x in range(meta_fields):
		meta_sum += unprocessed_part.pop(0)

	return meta_sum, unprocessed_part

start_time = time()

parsed_document = list(map(int, document.split(' ')))
total_sum, unprocessed_part = parse_child(parsed_document)

print('Solution', total_sum)

print('Finished in', time() - start_time)
