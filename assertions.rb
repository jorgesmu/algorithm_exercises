module Assertions

	def assert_equal(expected, result)
		print("Failed expectation #{expected} != #{result}") unless expected == result
	end
end