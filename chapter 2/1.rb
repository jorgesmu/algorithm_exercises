require('./list.rb')
require('set')

n = Node.new(5)
n.appendToTail(5)
n.appendToTail(5)

n.appendToTail(5)

n.appendToTail(1)
n.appendToTail(1)
n.appendToTail(6)
n.appendToTail(80)
n.appendToTail(10)

n.appendToTail(6)
n.appendToTail(80)
n.appendToTail(10)

#we can do it in N if deleting while checking without using the method defined in class
#this is O(n^2)
# node = n 
# set = Set.new 
# set.add node.data
# while(node.next)  do # n times do it
#     node = node.next
#     if set.include?(node.data)
#         puts "borro"
#         n = n.delete_node node.data #this executes in n
#     end
#     set.add node.data
# end

# without temporal buffer I can sort it and then apply the same algorithm but useing O(n)
node  = n 
while(node) do
    compared_node = node.next
    previous = node
    while(compared_node) do
        if node.data == compared_node.data
            previous.set_next  compared_node.next
            compared_node = compared_node.next
        else
            previous = compared_node
            compared_node = compared_node.next
        end
    end
    node = node.next
end

