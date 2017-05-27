require('./list.rb')
require('set')
n1 = Node.new(3)
n2 =Node.new(1)
n3 =Node.new(4)
n4 =Node.new(9)
n5 =Node.new(2)

n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
n5.set_next(n3)

#O(n) , memory 2n
def first_node_of_loop(node)
  return nil if not node
  set = Set.new
  while(node)
    if set.include? node.object_id
      return node
    end
    set.add node.object_id
    node = node.next
  end
  return nil
end

res = first_node_of_loop n1
