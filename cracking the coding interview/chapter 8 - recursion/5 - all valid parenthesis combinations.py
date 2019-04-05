# Being n the number of parenthesis
# We can in every carachter make a desicion: to add a open parenthesis or a closing one
# there are 2^(n+1) combinations given that n represent pairs.
# O(2^n)
# if close < open means we are in an valid combination
def calculate_combinations(combinations, current_string, open, close):
	if close < open or open < 0 or close < 0:
		return
	if open == 0 and close == 0:
		combinations.append(current_string)
		return
	calculate_combinations(combinations, current_string + ")", open, close-1)
	calculate_combinations(combinations, current_string + "(", open-1, close)


def parenthesis_combinations(n):
	combinations = []
	calculate_combinations(combinations, '(', n-1,n)
	return combinations

print(parenthesis_combinations(3))