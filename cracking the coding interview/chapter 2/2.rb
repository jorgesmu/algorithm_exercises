require('./list.rb')

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

def Nth(list, n)
    cont=1
    node = list
    nth_node=list
    while(cont<=n) do
        nth_node = nth_node.next
        cont+=1
    end
    while (not nth_node.nil?) do
        node = node.next
        nth_node = nth_node.next
    end
    node
end

puts(Nth n, 3)