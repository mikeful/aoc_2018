from data import document
from time import time

def parse_child(unprocessed_part, level=1):
	node_value = 0
	child_sums = {}
	child_nodes = unprocessed_part.pop(0)
	meta_fields = unprocessed_part.pop(0)

	if child_nodes > 0:
		# Child nodes found, get sub node values
		for index in range(child_nodes):
			sub_node_value, unprocessed_part = parse_child(unprocessed_part, level+1)
			child_sums[index + 1] = sub_node_value

		# Process meta fields as indexes
		for x in range(meta_fields):
			meta_value = unprocessed_part.pop(0)
			try:
				node_value_add = child_sums[meta_value]
			except KeyError as e:
				node_value_add = 0
			node_value += node_value_add
	else:
		# No child nodes found, use meta field sum as node value
		for x in range(meta_fields):
			meta_value = unprocessed_part.pop(0)
			node_value += meta_value

	return node_value, unprocessed_part

start_time = time()

parsed_document = list(map(int, document.split(' ')))
total_value, unprocessed_part = parse_child(parsed_document)

print('Solution', total_value)

print('Finished in', time() - start_time)
