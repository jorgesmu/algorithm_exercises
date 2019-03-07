# Problem given a sequence of parenthesis, whats the minimum amount of
# extra parethesis that will need to be added, even close of open parethesis
# to both left and right of the sequence to make if valid

# Examples
# ()() => 0
# ()( => 1
# )( => 2
# (((()( => 4
# )))()(() => 4
# ()))) => 3
# )))()(() => 4
# (()( => 1


# This solution is O(n) and just uses two ints to solve it
# which is constant and small
def missing_parenthesis(input):
	if len(input) == 0 or type(input) != str:
		return 0
	current_opens = closing_missing = 0
	for parethesis in input:
		if parethesis not in ['(', ')']:
			raise Exception('Invalid input')
		if parethesis == '(':
			current_opens += 1
		else:
			if current_opens > 0:
				current_opens -= 1
			else:
				closing_missing += 1
	return current_opens + closing_missing

print(missing_parenthesis('()()'))
print(missing_parenthesis('()('))
print(missing_parenthesis(')('))
print(missing_parenthesis('(((()('))