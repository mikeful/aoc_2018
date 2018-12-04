from data import date_log
from time import time
import re, operator

log_pattern = re.compile('\d{2} (?P<hour>\d{2}):(?P<minute>\d{2})\] (Guard #(?P<guard_id>\d+))? ?(?P<message>.+)')
is_sleeping = re.compile("falls")
is_waking = re.compile("wakes")
guard_total = {}
guard_minutes = {}
last_guard_id = None
last_sleep_min = 0
last_wake_min = 0

def parse_row(row_string):
	match = log_pattern.search(row_string)

	data = {
		'message': match.group('message'),
		'guard_id': match.group('guard_id')
	}

	if match.group('hour') == '23':
		data['hour'] = 0
		data['minute'] = 0
	else:
		data['hour'] = int(match.group('hour'))
		data['minute'] = int(match.group('minute'))

	return data

start_time = time()

date_log.sort()
for entry in list(map(parse_row, date_log)):
	# Check for new shift
	if entry['guard_id']:
		last_guard_id = entry['guard_id']
		if last_guard_id not in guard_total:
			guard_total[last_guard_id] = 0
			guard_minutes[last_guard_id] = [0 for x in range(60)]

	# Check sleep/wake status
	if is_sleeping.search(entry['message']) != None:
		last_sleep_min = entry['minute']
	if is_waking.search(entry['message']) != None:
		last_wake_min = entry['minute']
		guard_total[last_guard_id] += last_wake_min - last_sleep_min
		for index in range(last_sleep_min, last_wake_min):
			guard_minutes[last_guard_id][index] += 1

# Get guard id with max sleep time and most slept minute
sleepiest_guard = max(guard_total.items(), key=operator.itemgetter(1))[0]
max_slept_minute, minute_amount = max(enumerate(guard_minutes[sleepiest_guard]), key=operator.itemgetter(1))

print(int(sleepiest_guard) * int(max_slept_minute))

print('Finished in', time() - start_time)
