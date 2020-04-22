country = input('請問你是哪國人:')
age = input('請輸入年齡:')
age = int(age)
if country == '台灣':
	if age >=18:
		print('你可以考駕照啦!')
	else:
		print('不能考駕照啦~')
elif country == '美國':
	if age >= 16:
		print('那妳可以開車 美國爸爸')
	else:
		print('再等一下喔喔喔')
else:
	print('不關我事情')
