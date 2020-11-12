# https://leetcode.com/problems/two-sum/

def twoSum(self, nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	mapping = {}
	for i in range(len(nums)):
		if nums[i] in mapping:
			mapping[nums[i]].append(i)
		else:
			mapping[nums[i]] = [i]
	for i in range(len(nums)):
		left = target - nums[i]
		if left in mapping:
			for j in mapping[left]:
				if j != i:
					return [i, j]
	return []



print(twoSum(1, [2,7,11,15], 9))