x = 3
while x >= 0:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功!')
		break 
	elif password != 'a123456':
		x = x-1
		print('密碼錯誤還剩',x,'次機會')
		if x <= 0:
			print('掰掰')
			break
