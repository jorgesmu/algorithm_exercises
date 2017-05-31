require('../chapter 2/list.rb')

class Stack

    def push element
        node = Node.new element
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

end
