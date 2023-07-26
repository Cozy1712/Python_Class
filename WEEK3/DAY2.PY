# temp = 0
# while temp != -1000:
#     temp = eval(input('Enter a temperature (-1000 to quit): '))
# print('In Fahrenheit that is', 9/5*temp+32)


# temp = 0
# while temp!=-1000:
#     temp = eval(input('Enter a temperature (-1000 to quit): '))
# if temp!=-1000:
#     print('In Fahrenheit that is', 9/5*temp+32)
# else:
#     print('Bye!')

# from random import randint
# guess = 0
# screte_num = randint(1,10)
# while guess != screte_num:
#     guess = eval(input('Guess a number: '))
# print('you won')


# temp = eval(input('Enter temperature in celsius: '))
# while temp < -273.15:
#     eval(input('Enter a valid temperature: '))
# print(9/5*temp+32)

# i = 0
# while i<=50:
#     print(i)
#     i=i+2
# print('Bye!')

# temp = 0 
# while temp!=-1000: 
#     temp = eval(input(': ')) 
#     if temp != -1000:
#      print(9/5*temp+32) 
# else: 
#     print('Bye!')

# while True:
#     temp = eval(input(': '))
#     if temp == -1000:
#         print('bye')
#         break
#     else:
#         print(9/5*temp+32)


# a,b,c=7,9,10
# bill = 23.60
# tip = 23.60*.25
# print('Tip: ${:.2f}, Total: ${:.2f}'.format(tip, bill+tip))

# FORMATING STRING 

s='12345'
num=len(s)
for i in range(1,num+1):
    print('{:^5d}'.format(int(s[:i])))

# pounds = 2.20462
# weight = 1
# while weight != 0:
#     weight = eval(input('enter your weight in kg: '))
#     if weight < 0:
#         print('entry invalid')
#     else:
#         print(weight*pounds)
#         break


limit = 0
password = 0
screte_word = 12345
while password != screte_word and limit <= 4:
    password = eval(input('Enter a password: '))
    limit += 1
    if password != screte_word:
        print('re-enter password')        
    else:
        print('logged in')
        break
    if limit == 5 and password != screte_word:
        print('kicked out')




l = []
count = 0
while True:
    score = eval(input('enter score or -1 to end: '))
    if score == -1:
        break
    l.append(score)
    count = [item for item in l if item>=90]
    count = len(count)
print('Scores that has A\'s are: ',count)
avg = sum(l)/len(l)
print(avg)
