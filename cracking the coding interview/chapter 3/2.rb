require('./../chapter 2/list.rb')

# I think that the improvement that the book does is only good if you assume you cant
# have duplicated values because if you have the min twice in the stack and you pop
# the first out of the stack it will change the min and thats not true.
# Its not a common case for a stack

class DataPair
  def initialize(value, min)
    @value = value
    @min = min
  end

  def value
    @value
  end

  def min
    @min
  end
end

class Stack

  def push value
    min = (@elements and @elements.data.min < value) ? @elements.data.min : value 
    data = DataPair.new value, min
    node = Node.new data
    node.set_next @elements
    @elements = node
    nil
  end

  def pop
    return nil if @elements.nil?
    element = @elements.data
    @elements = @elements.next
    element
  end

  def min
    return nil if @elements.nil?
    @elements.data.min
  end

end
