# Taken from: https://www.youtube.com/watch?v=c0OMPDLef08&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj

def fizzBuzz(x):
	if x < 1:
		return
	for i in range(1, x+1):
		line = ''
		if i % 3 == 0:
			line+='Fizz'
		if i % 5 == 0:
			line+=('Buzz')
		if line == '':
			line+=str(i)
		print(line)
	return

fizzBuzz(47)