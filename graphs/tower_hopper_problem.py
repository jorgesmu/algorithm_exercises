# Taken from: https://www.youtube.com/watch?v=kHWy5nEfRIQ&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=13
# O(len(towers)+number_of_hops) and taking O(n+hops) extra space
def is_hoppeable(towers):
	if len(towers) == 0:
		return False
	visited = [False for i in range(len(towers))]
	queue = [0]
	found = False
	while len(queue) > 0 and not found:
		current_step = queue.pop(0)
		if not visited[current_step]:
			for next_step in range(1, towers[current_step] + 1):
				if (current_step + next_step) == len(towers):
					return True
				elif (current_step + next_step) <= len(towers) and not visited[current_step+next_step]:
					queue.append(current_step+next_step)
			visited[current_step] = True
	return found

towers = [4, 2, 0, 0, 2, 0]
print('is_hoppeable for ', towers, ':')
print(is_hoppeable(towers))


towers = [1, 0]
print('is_hoppeable for ', towers, ':')
print(is_hoppeable(towers))


# solution propoused by the video
def next_step(towers, step):
	if towers[step] == 0:
		return None
	max = result_step = 0
	for i in range(step+1, step + towers[step] + 1):
		if i == len(towers):
			return i
		if i + towers[i] > max:
			max = i + towers[i]
			result_step = i

	return result_step


def is_hoppeable_range(towers):
	best_step = next_step(towers, 0)
	while(best_step and best_step != len(towers)):
		best_step = next_step(towers, best_step)

	if best_step:
		return True
	return False


towers = [4, 2, 0, 0, 2, 0]
print('is_hoppeable_range for ', towers, ':')
print(is_hoppeable_range(towers))


towers = [1, 0]
print('is_hoppeable_range for ', towers, ':')
print(is_hoppeable_range(towers))