import random
r = random.randint(1,100)

while True:
	num = input('請猜一個數字:')
	num = int(num)
	if num == r:
		print('水喔!')
		break
	elif num > r:
			print('小一點')
	elif num < r:
			print('大一點')

