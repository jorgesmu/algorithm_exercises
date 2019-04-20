# Taken from: https://www.youtube.com/watch?v=LFAhxzqvyps&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=28

def clock_angle(hour, minutes):
	if hour < 0 or hour > 11 or minutes < 0 or minutes >= 60:
		raise Exception('invalid hour')

	minute_angle = 6*minutes # 360/60 = 6 degrees
	hour_angle = 30*(hour + minutes/60) # 360/12=30
	angle = abs(minute_angle -  hour_angle)
	return min(angle, 360-angle)

def execute(hour, minute):
	print('hour: ', hour, ' minute: ', minute, ' angle: ', clock_angle(hour, minute))

execute(0, 0)
execute(10, 55)
execute(0, 15)
execute(0, 30)
execute(0, 45)
execute(0, 59)
execute(3, 45)
execute(11, 10)