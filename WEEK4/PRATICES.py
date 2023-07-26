# country=[line.strip() for line in open('./WEEK/country.txt')]
# print(country)
# f = open('./WEEK/country1.txt', 'w')
# print('Ghana', file=f)
# print('Turkey', file=f)
# print(country)
# count=0
# for c in country:
#     c=c.lower()
#     if c[0] in 'aeoui':
#         count+=1
# print(round(count*100/len(country), 2))
        
        

#   FUNCTION 


def showAge():
    print('my age is 34')
showAge()

def square4():
    print('the square of 4 is ', 16)
square4=square4()

def square(n):
    return n*n

result=square(6)*6
print(result)

print(square(5))

def add(x,y=5):
    return x+y

print(add(45,100))

def showString(str1, str2):
    print(str1,str2)
    
showString(str2='Lagos', str1='oyo')

def func1(x):
    x = x + 1
    return x
def func2(L):
    L = L + [1]
    return L
a=3
M=[1,2,3]
print(func1(a))
print(func2(M))
print(a)
print(M)

# def add_excitement():
#     l=[]
#     for i in range(5):
#         entry = input('enter a string: ')
#         l.append(entry)
#     s = [word + '!' for word in l[:]]
#     print(s)
# add_excitement()

    # def add_excitement():
    #     l=[]
    #     for i in range(5):
    #         entry = input('enter a string: ')
    #         l.append(entry)
    #     return l
    # print(add_excitement())
    
def digital_root(n):
    sum = 0
    while n > 0 or sum > 9:
        if (n == 0):
            n = sum
            sum = 0
        elif (n > 0):
            sum = sum + (n % 10)
            n = n/10
    
    print(sum)
digital_root(45893) 


def first_diff(str1, str2):
    if str1 == str2:
        return -1
    count = 0
    for a, b in zip(str1,str2):
        if a != b:
            break
        count +=1
    return count
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
print(first_diff(str1, str2))
        
       