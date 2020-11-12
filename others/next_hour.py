def find_next(digits, first, second, first_limit, second_limit):
	min_last = min_first = float('inf')
	for digit in digits:
		if digit > second and digit < min_last and digit <= second_limit:
			min_last = digit
	if min_last != float('inf'):
		return "{}{}".format(first, min_last)

	for digit in digits:
		if digit > first and digit <= first_limit and digit < min_first:
			min_first = digit
	if min_first != float('inf'):
		return "{}{}".format(min_first, min(digits))
	return None

def next(hour):
	digits = [int(hour[0]), int(hour[1]), int(hour[3]), int(hour[4])]
	next_min = find_next(digits, digits[2], digits[3], 5, 9)
	if next_min:
		return "{}{}:{}".format(digits[0], digits[1], next_min)
	next_hour = find_next(digits, digits[0], digits[1], 2, 3)
	min_digit = min(digits)
	if next_hour:
		return "{}:{}{}".format(next_hour, min_digit, min_digit)
	return "{}{}:{}{}".format(min_digit, min_digit, min_digit, min_digit)

print(next('23:59'))