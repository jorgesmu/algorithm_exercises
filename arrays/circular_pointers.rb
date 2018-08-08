# Exersice taken from https://www.youtube.com/watch?v=VX2oZkDJeGA	

# This is a graph approach. Both of them are O(n). 
# This approach uses more memory - n - in the worst case but 
# is easier to understand and mantain for other developers.
# Depending on the size of the array this would be a problem or not.
# We can also use a set for checking the visited to make it more efficient
def circular_graph?(array)
	return false if array.size.zero?
	visited = array.size.times.map{ |i| false }
	visited[0] = true

	array.each do |index|
		if index > array.size 
			return false
		end

		if visited[index]
			return true
		end

		visited[index] = true
	end
	false
end

array = [1, 2, 1, 3, 4, 8]

puts "Array is #{circular?(array) ? '' : 'not '}circular "