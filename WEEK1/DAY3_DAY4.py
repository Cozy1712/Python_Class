# if statement  and conditinal operators
# comparison operators ==, >, <, >=, <=, !=

# users = eval(input('Enter length in centimeter: '))
# inch = (users//2.54)
# if users == abs(users):
#     print(inch)
# else:
#     print('invalid entry')

# user_1 = eval(input('Enter temperature amount: '))
# units = input('enter unit, celsius or fahrenheit: ')
# f = (((9//5)* user_1) + 32)
# c = (5//9)*(user_1-31)
# if units == 'C':
#     print(f,'F',sep='')
# elif units == 'F':
#     print(c,'C',sep='')
# else:
#     print('invalid unit')

# user_2 = eval(input('how many credit have you taken: '))
# if user_2 <= 23:
#     print('student is a freshman')
# elif user_2 <=53:
#     print('They are a sophomore')
# elif user_2 <= 83:
#     print('junior')
# else:
#     print('seniors')

#assignment 2,3,4,5,6 
import math
from random import randint
count = 0
for i in range(1,100):
    if (i ** i) % 10 == 4:
        count+=1
print(count)

# n = eval(input('Enter a value: '))
# sum = 0 
# for i in range(1,n+1):
#     sum = sum + (1/i)
#     sum - math.log(n)
# print(round(sum,2))

# sum = 0 
# for i in range(1,2000):
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i
# print(sum)


# num = eval(input('Enter a number: '))
# sum = 0
# for i in range(1, num+1):
#     if (num % i == 0):
#         sum += i
#         print(i)
# print('The sum of the divisor is',sum)


# for i in range(1, 500):
#     sum = 1
#     for n in range(2, i):
#         if (i % n == 0 and n != i ):
#             sum+=n
#     if sum == i:
#         print(i)
# 


      # SWAPING THREE VARIABLES
x = 2
y = 3 
z = 4

x,y,z = y,z,x   # SWAP  VARIABLE

print('x =', x)
print('y =', y)
print('z =', z)


count1 = 0
count2 = 0
count3 = 0
for i in range(1, 1000):
    if ( i**(1/2)**2 == i):
        count1+= 1
    elif ( i**(1/2)**3 == i):
        count2 += 2
    elif ( i**(1/2)**5 == i):
        count3 += 2
print(1000-(count1+count2+count3))