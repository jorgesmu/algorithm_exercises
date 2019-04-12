# taken from: https://www.youtube.com/watch?v=xY65bgfXJTk
# valid ({[

#O(n) as iterating over the string only once
def valid_parenthesis(string):
	open =  [ '(', '{', '[']
	close = {
		'}': '{',
		')': '(',
		']': '['
	}
	stack = [] # Using a list as a stack
	for i in range(len(string)):
		char = string[i]
		if char in open:
			stack.append(char)
		elif char in close:
			if len(stack) == 0 or stack[-1] != close[char]:
				return False
			stack.pop()
	return len(stack) == 0

def execute(string):
	print('valid_parenthesis for string: ', string, 'is: ', valid_parenthesis(string))

execute('asdfasdfadfaf')
execute('{}()[]')
execute('{}()][]')
execute('{({)})][]')
execute('{asdfa}asdfa(asdf)[]')
execute('{asdfa}asdfa(asdf)[][')