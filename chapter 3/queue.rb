require('../chapter 2/list.rb')

class QueueDataStructure #there is athor queue for threads defined by default in ruby

    def queue element
        if @first.nil?
            @first = Node.new element
            @last = @first
        else
            @last.set_next  Node.new element
            @last = @last.next
        end
    end

    def unqueue
       return nil if not @first
       element = @first
       @first = @first.next
       element.data
    end
end