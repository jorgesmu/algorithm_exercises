require('./list.rb')

n1 = Node.new(3)
n1.appendToTail(1)
n1.appendToTail(4)
n1.appendToTail(9)

n2 = Node.new(5)
n2.appendToTail(9)
n2.appendToTail(6)

# n = size of n1, m= size of n2
# this implementation is O(n+m)
def sum(n1, n2, overflow=false)
  return nil if n1.nil? and n2.nil? and not overflow
  digit_sum = overflow ? 1 : 0 
  if n1 and n2
    digit_sum+= n1.data + n2.data
  elsif n1 or n2
    digit_sum+= (n1||n2).data
  end
  result = Node.new (digit_sum%10)
  overflow = digit_sum>=10 ? true : false

  result.set_next(sum( (n1 ||  Node.new(nil) ).next, (n2 || Node.new(nil) ).next, overflow))
  result
end

res = sum n1, n2
