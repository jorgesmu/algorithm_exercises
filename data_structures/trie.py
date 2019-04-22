# Taken from: https://www.youtube.com/watch?v=NZ3lP33mXlY&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=46

class Node:
	def __init__(self, prefix):
		self.prefix = prefix
		self.children = {}
		self.is_word = False

class Trie:
	def __init__(self, dictonary):
		self.head = Node('')
		for word in dictonary:
			if len(word) > 0:
				self.__insert_word(word)

	def __insert_word(self, word):
		if len(word) == 0:
			return
		pointer = 0
		current_node = self.head
		while pointer < len(word):
			current_char = word[pointer]
			if not current_char in current_node.children:
				current_node.children[current_char] = Node(word[0:pointer+1])
			current_node = current_node.children[current_char]
			pointer+=1
		current_node.is_word = True

	def words_for(self, prefix):
		current_node = self.head
		for char in prefix:
			if not char in current_node.children:
				return []
			current_node = current_node.children[char]
		return self.__find_words_for(current_node)

	def __find_words_for(self, node):
		queue = [node]
		results = []
		while len(queue) > 0:
			current_node = queue.pop(0)
			if current_node.is_word:
				results.append(current_node.prefix)
			for k in current_node.children:
				queue.append(current_node.children[k])
		return results


