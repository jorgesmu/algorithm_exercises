# Excersice taken from: https://www.youtube.com/watch?v=B6Tsrmgsy3k


# Assumptions:
# - sorted arrays of integers
# - arrays without repeats

array1 = [2,6,9,11,13,17]
array2 = [3,6,7,10,13,18]
array3 = [4,5,6,9,11,13]

IDX_OVERFLOW = 'IDX_OVERFLOW'

def target_idx(array, current_idx, value)
  while array[current_idx] < value
    current_idx += 1
    if current_idx == array.size
      return IDX_OVERFLOW
    end
  end
  current_idx
end

def intersections(array1, array2, array3)
  intersection = []
  return intersection if array2.size.zero? || array3.size.zero?
  idx2 = idx3 = 0

  array1.each do |array1_element|
    idx2 = target_idx(array2, idx2, array1_element)
    idx3 = target_idx(array3, idx3, array1_element)

    # if iteration is over on one of the arrays, then 
    # there are no other elements belonging to the intersection
    if idx2 == IDX_OVERFLOW || idx3 == IDX_OVERFLOW
      return intersection
    end

    if array2[idx2] == array1_element && array3[idx3] == array1_element
      intersection.push array1_element
    end
  end
  intersection
end

puts intersections(array1, array2, array3)