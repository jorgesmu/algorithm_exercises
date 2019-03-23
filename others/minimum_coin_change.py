# Solution id O(value*coings)
def coin_change(value, coins):
	coins_per_value = [-1 for i in range(value+1)] 
	coins_per_value[0] = 0
	for vi in range(1, value+1):
		min = float("inf")
		for coin in coins:
			if coin <= vi:
				coins_in_path = coins_per_value[vi-coin]
				if coins_in_path >= 0 and (coins_in_path + 1) < min:
					min = coins_in_path + 1
		coins_per_value[vi] = min
	return coins_per_value[value] if coins_per_value[vi] != float("inf") else None

coins = [2, 5]
value = 15
print(coin_change(value, coins))
