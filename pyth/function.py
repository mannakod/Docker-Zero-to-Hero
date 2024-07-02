def myfun(user, age=None):
	print('*' * 20)
	print(f'Welcome {user}')
	print('Hello, running from fucntion')
	print(f'welcome   {age}')
	print('*' * 20)
#myfun()


myfun('raju', 30)

myfun('manish')
################

def myfun2(user, *hobbies):
	print(f'welcome {user}')
	print('your hobbies are: ')
	for hobby in hobbies:

	 print(f'- {hobby}')

myfun2('Raju', 'Sing', 'Dance', 'Cricket')

##################3
def add(num1, num2):
	return num1 + num2
	#result = num1 + num2
	#return result
	#print(result)


print(add(10,20))
result =add(10, 40)
print(result)
