# Taken from: https://www.youtube.com/watch?v=LBsvAwQbVdw&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=47

def int_to_roman_numeral(num):
	if num <= 0 or num > 3999:
		raise Exception('invalid input')
	translation = {
		'M': 1000,
		'CM': 900,
		'D': 500,
		'CD': 400,
		'C': 100,
		'XC': 90,
		'L': 50,
		'XL': 40,
		'X': 10,
		'IX': 9,
		'V': 5,
		'IV': 4,
		'I': 1,
	}
	result = ''
	while num > 0:
		for roman in translation:
			if num >= translation[roman]:
				times = int(num/translation[roman])
				for i in range(times):
					result+=roman
				num = num - times*translation[roman]
	return result

def execute(num):
	print('num ', num, ' to roman is: ', int_to_roman_numeral(num))

execute(58)
execute(3658)
execute(9)
execute(499)