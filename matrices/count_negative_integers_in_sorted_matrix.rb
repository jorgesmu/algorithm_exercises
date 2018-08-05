# excersice taken from: https://www.youtube.com/watch?v=5dJSZLmDsxk

# Naive approach O(n)
require 'matrix'

matrix = Matrix[[-3, -2, -1, 1], [-2, 2, 3, 4], [4,5,7,8]]

def negatives_in_col(matrix, col)
	# Count negatives in col
	negative_count = 1 # if the code reach here it mean the first element is negative no need to recheck it
	if matrix.row_count == 1
		return negative_count
	end
	for row in (1..(matrix.row_count-1)) do
		if matrix[row, col].negative?
			negative_count+=1
		else
			return negative_count
		end
	end
	negative_count
end

def negative_matrix_count(matrix)
	col = 0
	negative_count = 0 
	still_negative_row = true

	# Find negative starting cols
	while(still_negative_row && col < matrix.column_count)
		if matrix[0,col].negative?
			negative_count += negatives_in_col(matrix, col)
			col+=1
		else
			still_negative_row = false
		end
	end
	negative_count
end

puts "Negative count cells: #{negative_matrix_count(matrix)}"