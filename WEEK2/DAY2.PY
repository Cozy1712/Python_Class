# # LISTS IN PYTHON
# from random import randint
# s = [1, 2, 3, 4, 6, 8, 7, 13, 12, 9, 5, 11]
# s.append(10)
# s.sort()
# s.reverse()
# s.remove(13)
# s.insert(0, 13)
# s.reverse()
# s.pop(3)
# print(s)
# m = s[:]
# print(m)
# M=m[:]
# M.append(34)
# print(m)
# print(M)
# L=[]
# for i in range(100):
#     L.append(randint(1, 100))
# print(L)

# # f=[]
# # for i in range(1, 101):
# #     f.append(L.count(i))
    
# # print(f)

# # l = []
# # for i in range(1, 6):
# #     num = eval(input('enter a number between 1 and 12: '))
# #     l.append(num)
# # for i in range(len(l)):
# #     if l[i]>10:
# #         l[i]=10
# # print(l)     


# k = [8,9,10]
# k[1]=17
# k.append(4)
# k.append(5)
# k.append(6)
# k.remove(8)
# k.sort()
# k.extend(k)
# k.insert(3,25)
# print(k)

from random import *

# my_list = choice(list)
# print(my_list)
# my_list = sample(list, 3)
# print(my_list)

from random import shuffle
# players = ['Joe', 'Bob', 'Sue', 'Sally']
# shuffle(players)
# for p in players:
#     print(p, 'it is your turn.')

# s = 'hi! this is kolawole akange,'
# from string import punctuation
# for c in punctuation:
#     s = s.replace(c, '')
# print(s.split())


# l=['A','B','C']
# y=''.join(l)
# print(y)


# word = input('Enter a word: ')

# letter_list = list(word)
# shuffle(letter_list)
# anagram = ''.join(letter_list)
# print(anagram)

num = eval(input('enter a number: '))
i = 0
while (i < (num+1)):
    j = 1
    while (j <= 12):
        j +=1
        print(i,'x', j, '=', i*j)
