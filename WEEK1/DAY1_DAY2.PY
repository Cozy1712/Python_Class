print('hello world')

# degree = eval(input('enter temp amount: '))
# print('in fat, that is', 9/5*degree+32)

# print('*'*20)
# print('*',' '*18, '*', sep="")
# print('*',' '*18, '*')
# print('*'*20)


# for i in range(6):
#     print('*'*i)
    
# deg = int(input('enter a number'))
# print( deg,deg*2,deg*3, deg*4, sep='---')

# for i in range(10):
#     print(i)
    
for i in range(11):
    print( i,'----', i**2 )

for i in range(6, 0, -1):
    print('*'*i)

print(round(3.336, 2))

import math
print(dir(math))

# EXersice: page 3.8(1,8,10,11);

#  Assignment
# for i in range(101):
#     print(i, 'kolawole')

# for i in range(21):
#     print(i,i**2, sep='----')

# #for i in range(8,100,3):
# #    print(i, end=' ')

# for i in range(102,1,-2):
#     print(i,end=' ')

# for i in range(1):
#     print('A'*5,'B'*4,'CD'*3,'E','F'*3,'G',sep='') 
    
# 

# finding last digit of 2 raised to that power
power = eval(input('Enter a power: '))
digit = eval(input('Enter how many digit: '))
result = math.pow(2, power)
last_digit = result % 10
lastTwo_digit = result % 100
manyDigit = (result %(pow(10,digit)))
print(result)
print(last_digit)
print(lastTwo_digit)
print(manyDigit)


#since 1kg can be expressed as 2.20462pounds
pounds = 2.20462
weight = eval(input('Enter your weight in kg: '))
result = (weight)*(pounds)
print('Your weight in pounds is',round(result, 10))
