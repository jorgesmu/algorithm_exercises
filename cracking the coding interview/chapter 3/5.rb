require('../chapter 2/list.rb')
require('../assertions.rb')
include Assertions

class Stack
  def initialize
      @size = 0
  end
  def push element
      node = Node.new element
      node.set_next @elements
      @size+=1
      @elements = node
      nil
  end

  def pop
      return nil if @elements.nil?
      element = @elements.data
      @elements = @elements.next
      @size-=1
      element
  end

  def size
      @size
  end

  def index index
      return nil if index < size
      iterator = 1
      node = @elements
      while(iterator < index) do
          node = node.next
          iterator +=1
      end
      node
  end
end

class MyQueue
  def initialize
    @queue_stack = Stack.new
    @unqueue_stack = Stack.new
  end

  def queue(element)
    # queue is O(1) just pushing into a stack
    @queue_stack.push(element) 
  end

  def unqueue
    # unqueue is O(n) + 1 in the worst case, need to migrate the entire stack 
    return @unqueue_stack.pop if @unqueue_stack.size > 0
    migrate_queues()
    @unqueue_stack.pop
  end

  private 

  def migrate_queues
    # Moving from one stack to the other in reverse order
    while(@queue_stack.size > 0) do
      element = @queue_stack.pop
      @unqueue_stack.push(element)
    end
  end
end


queue = MyQueue.new

assert_equal(nil, queue.unqueue)

queue.queue 1
queue.queue 2
queue.queue 3
assert_equal(1, queue.unqueue)
assert_equal(2, queue.unqueue)
assert_equal(3, queue.unqueue)

queue.queue 4
queue.queue 5
queue.queue 6
assert_equal(4, queue.unqueue)

queue.queue 7
queue.queue 8
queue.queue 9
assert_equal(5, queue.unqueue)
assert_equal(6, queue.unqueue)
assert_equal(7, queue.unqueue)
assert_equal(8, queue.unqueue)
assert_equal(9, queue.unqueue)
assert_equal(nil, queue.unqueue)
puts 'Finished expectations'