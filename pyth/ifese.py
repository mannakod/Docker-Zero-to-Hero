age = int(input('Enter your age: '))
Voter_ID = input('Do you have voter id? enter Y or N:')
#my = True
#print(type(my))
#confirm = 
#you can use and operator
if age > 18:
 if Voter_ID == 'Y':
  print('you can vote')
 else:
  print('Please apply for voter id')

else:
 print('you cant vote')



if age % 2 == 0:
 print('Yes number is even')
else:
 print('Number odd :( ')


users=['paul', 'sham', 'gopi']


if 'pausl' in users:
	print('users exist')
else:
	print('not exists')
