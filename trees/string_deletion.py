# Taken from: https://www.youtube.com/watch?v=A6fDK8Vc7-U&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=32
from tree import Tree

def delete(query, dictonaty):
	seen_path = set([query])
	queue = [query]
	while len(queue) > 0:
		current_element = queue.pop(0)
		seen_path.remove(current_element)
		if current_element in dictonaty:
			return len(query) - len(current_element)
		for i in range(len(current_element)):
			current_branch = current_element[0:i] + current_element[i+1:len(current_element)]
			if current_branch not in seen_path and len(current_branch) > 0 :
				seen_path.add(current_branch)
				queue.append(current_branch)
	return -1

dictonary = ['a', 'aa', 'aaa', 'aba']
query = 'abcba'
print('dictonary: ', dictonary)
print('query: ', query)
print('delete: ', delete(query, dictonary))