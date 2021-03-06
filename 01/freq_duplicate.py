from data import changes

frequency = 0
seen_frequencies = set([0])

while True:
	for change in changes:
		frequency += change

		if frequency in seen_frequencies:
			print('Frequency already seen:', frequency)
			exit()
		else:
			seen_frequencies.add(frequency)
