require('./list.rb')

n = Node.new(5)
n.appendToTail(67)

n.appendToTail(1)
n.appendToTail(4)

n.appendToTail(6)
n.appendToTail(80)
n.appendToTail(10)

element = n.next.next.next

def delete_node(element)
  if element.nil? or element.next.nil?
    return false 
  end
  element.set_data(element.next.data)
  element.set_next(element.next.next)
  true
end

delete_node element