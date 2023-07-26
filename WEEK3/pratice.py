# READING TEXT FILES

# lines = [line.strip() for line in open('./WEEK3/content.txt')]
# print(lines)

# wordlist = [line.strip() for line in open('wordlist.txt')]

# for word in wordlist:
#     if word[:-3] == 'ime':
#         print(word)
        
def word_list():
    print('hello!')
    
word_list()

def draw_square(n):
    for i in range(2):
        print('*' *n)
        print('*', ' '*n, '*')
        print('*', ' '*n, '*')
        print('*'*n)

draw_square(15)

from math import pi, sin
def deg_sin(x):
    return sin(pi*x/180)
# x = 4
print(deg_sin(4))

def func1():
    for i in range(10):
        print(i)
# func1()
def func2():
    i = 100
    func1()
    print(i)
func1()
func2()
def rectangle(m,n):
    for row in range(m):
        for col in range(n):
            print('*',end='')
        print('')
rectangle(2,4)


l = ['boy','bag', 'shoe']
def add_excitement():
    strings = [word + '!' for word in l]
    print(strings)
add_excitement()

# def add_excitement():
#     entry = input('enter a string: ')
#     return entry     
# print(add_excitement())



def sum_digit():
    num = 2
    return num + num
print(sum_digit())

  
def factors():
    list_factors = [] 
    num = eval(input('enter an integer: '))
    for i in range(1, num+1):
        if num % i == 0:
            list_factors.append(i)
    return list_factors
print(factors())  

       
def number_of_factors():
    factors = []
    num = eval(input('Enter an integer: ')) 
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return len(factors)      
print(number_of_factors())  
