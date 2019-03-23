# We want to count how many different combinations there are
# O(v*coins)
def coin_change_combinations(v, coins):
	coins_buffer = [0 for vi in range(v+1)]
	coins_buffer[0] = 1
	for coin in coins:
		for vi in range(v+1):
			if coin <= vi:
				coins_buffer[vi] += coins_buffer[vi-coin]
	return coins_buffer[v]

coins = [1, 2, 5]
value = 12
print(coin_change_combinations(value, coins))