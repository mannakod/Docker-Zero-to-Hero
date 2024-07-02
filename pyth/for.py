'''
for i in (cat file.txt) :
	print(i)
'''

with open('file.txt', 'r') as file:
    for line in file:
        print(line)


user_list=['manish', 'kiran', 'haresh']
for user in user_list:
 print(user)



for num in range(0, 10):
 print(num)
