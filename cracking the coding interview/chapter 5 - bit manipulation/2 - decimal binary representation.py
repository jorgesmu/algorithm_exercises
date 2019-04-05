def to_bin(fpn):
	fpn_int = int(fpn[0:fpn.index('.')])
	fpn_dec = float(fpn) - fpn_int
	bin_int = ''
	while fpn_int > 0:
		if fpn_int % 2 == 0:
			bin_int = '0' + bin_int
		else:
			bin_int = '1' + bin_int
		fpn_int = fpn_int>>1
	bin_dec = ''	
	while fpn_dec > 0:
		if len(bin_dec) > 32:
			return 'ERROR'
		fpn_dec*=2
		if fpn_dec >= 1:
			bin_dec+= '1'
			fpn_dec-=1
		else:
			bin_dec+='0'


	return str(bin_int) + '.' + str(bin_dec)


print('3.0625 in bin is:', to_bin('3.0625'))
print('3.999 in bin is:', to_bin('3.999'))
print('45.75 in bin is:', to_bin('45.75'))