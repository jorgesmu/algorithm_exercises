# Taken from: https://www.youtube.com/watch?v=WqV-pxNUAYA&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=44
# solution also taken from the video

def visit(dependency, dependencies, temporary_marks, permanent_marks, result):
	if dependency in temporary_marks:
		raise Exception('invalid dependency topology')
	if not dependency in permanent_marks:
		temporary_marks.add(dependency)
		for i in depencencies[dependency]:
			visit(i, depencencies, temporary_marks, permanent_marks, result)
		permanent_marks.add(dependency)
		temporary_marks.remove(dependency)
		result.append(dependency)

# This is O(n)
def build_order(depencencies):
	temporary_marks = set()
	permanent_marks = set()
	result = []

	for i in range(len(depencencies)):
		if i not in permanent_marks:
			visit(i, depencencies, temporary_marks, permanent_marks, result)
	return result

depencencies = [
	[],
	[0],
	[0],
	[1, 2],
	[3],
]
print(build_order(depencencies))