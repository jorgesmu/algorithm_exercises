require('../chapter 2/list.rb')

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

class SetOfStacks
    def initialize threadhole
        @threadhole=threadhole
        @stacks=[Stack.new]
    end

    def push value
        if @stacks[@stacks.size-1].size >= @threadhole
            @stacks.push Stack.new
        end  
        @stacks[@stacks.size-1].push value
        nil
    end

    def pop
        value = @stacks[@stacks.size-1].pop
        delete_stack_if_empty(@stacks.size-1)
        value
    end

    def pop_at index
        return nil if index >= @stacks.size  or index < 0 
        value = @stacks[index].pop
        delete_stack_if_empty index
        value
    end

    private 

    def delete_stack_if_empty index
        if @stacks[index].size == 0 and @stacks.size>1
            @stacks.delete_at(index)
        end
        nil
    end
end
