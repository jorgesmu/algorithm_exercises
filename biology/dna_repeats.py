#For example, given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", return: ["AAAAACCCCC", "CCCCCAAAAA"].

# Problem taken from: https://www.programcreek.com/2014/03/leetcode-repeated-dna-sequences-java/
# If I check all old sequences for slice of size 10 I will be memory efficient. But will will be O(n^2)/slice-size
# If I keep memory of all seen slices in worth case scenario (I see all differnt slices) I will have 4^10 combinations
# of sequences of 10 letters dna (lets assume 10B) which is 10*(10^4)Bytes which is ~= 10.5MB which is managable for todays
# current memory limits. If we need frequencies we can use a hashtable with the same order of magnitude.


# I also assume we are just interested in the repetitions and not the frequency, so I will return a set which worst case 
# scenario will duplicate memory usage but is still (~= 21MB) which is reasonable. This solucion is O(n) as we iterate
# only once through the string. In memory is O(20*(4^10))

def find_repeats(dna_sequence, slice_window_size):
	if len(dna_sequence) <= slice_window_size:
		return []
	seen_sequences = set()
	repeated_sequences = set()

	for i in range(0, len(dna_sequence) - (slice_window_size - 1)):
		current_slice = dna_sequence[i:i+slice_window_size]
		# Testing using in operator is O(1) in python
		if current_slice in seen_sequences:
			target_set = repeated_sequences
		else:
			target_set = seen_sequences
		# Adding to a set is O(1)
		target_set.add(current_slice)
	return repeated_sequences

dna_sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
slice_window_size = 10
print(find_repeats(dna_sequence, slice_window_size))

# Conclusion:
# The java solution exposed here follows the exact same logic propoused here. The difference (in this case),
# that being dna 4 digits code(2^2) and being able to represent it with bits each letter of dna will take 2 bits in memory
# instaed of 1B. But all the others procedures and conclusions are valid and based on the same approach
