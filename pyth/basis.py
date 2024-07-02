print ('this is example of pyhton on linux')
#print('manish')

#use f for format, it will result string and calculation
print(f'Sum of two number are {10+20}')

name='manish'
number1=30
number2=20

total=(number1+number2)
#when use  string and calculation use f and {} as below
#other way
print(f'Total is number1 and number2 is {number1+number2}')
print(total)
#print with variable and string
print (f'my name is {name}')
num1 = 10
num2 = '10'
#find variable type
print(type(num1))
print(type(num2))

f_name = 'Paul'
l_name = 'Philip'
fullName = f_name + ' ' + l_name
#converts into capital
print(fullName.upper())
#convers into lower
print(fullName.lower())
#converts into first letter capital
msg='hello world! is my first program'
print(msg.title())
#slit from sentence

print(msg.split())

#to split in two parts
print(msg.split('!'))
print(msg[0])

#storing in master output of msg.str. where he gets space, it will devde
merastr =  msg.split()
#storing single character and printing 4th char
print(msg[0:4])
#printing 2 words from masterstr
print(merastr[0:2])
#printing one word from masterstr
print(merastr[0])




users = ['Haresh', 'Manish', 'Kiran']
#prints 0 postition
print(users)
print(users[-1])
print(users[0:2])

users.append('Manthan')

print(users)
#removing user from list with Name
users.remove('Manthan')
print (users[0])
print(users)
#updating user in list specific position
users[1] = 'Mannu'
print(users)
#add at specific place
users.insert(1, 'Manthan')
print(users)

#delete user from list
del users[1]
print(users)

#to sort without changing user list
print('sorted here')
print(sorted(users))
print(users)
print(len(users))


#sorting of list iteams
users.sort()
print(users)
#for revers
users.sort(reverse=True)
print(users)

print(users)
users.reverse()
print (f'reversing {users}')
#to remove last value
users.pop()
print(users)



marks = [45, 79, 90, 23, 10, 49, 99]

print (min(marks))
print (max(marks))
print (sum(marks))
print(sorted(marks))


mix_list = ['Paul', 19, 40, 54, 23, True]

#print(sorted(mix_list))
