class Node
    def initialize(data)
        @data = data
        @next = nil
    end

    def appendToTail(data)
        last_node = self
        while (last_node.next) do
            last_node = last_node.next
        end
        last_node.set_next(Node.new(data))
    end

    def data
        @data
    end

    def next
        @next
    end

    def set_data(data)
        @data=data
    end

    def set_next(next_node)
        @next = next_node
    end

    def delete_node(value)
        node = self
        
        if (node.data == value )
            return node.next
        end

        while(not node.next.nil?) do
            if (node.next.data == value)
                node.set_next  node.next.next
                return self
            end
            node = node.next
        end
        
        self
    end

end