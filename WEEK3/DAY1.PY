s = 'Hi! This is a test.'
print((s.split()))
date="3/4/2023"

print(int(date.split('/')[-1])-2001)

listDate=['1', '800', '271', '8281']
print('-'.join(listDate))

l='there'
letter=list(l)
from random import shuffle
for i in range(len(letter)):
    shuffle(letter)
    
    print(''.join(letter))
    
print([i**2 for i in range(1,6)])

L = [[1,2,3],[4,5,6],[7,8,9]]
s = [j for M in L for j in M]
print(s)
for r in range(len(L)):
    for c in range(3):
        print(L[r][c], end=" ")
    print()
   
    
print(len(L))
count=0
for i in range(len(L)):
    count+=len(L[i])
print(count)

n=sum([1 for i in range(len(L)) for c in range(len(L[i]))])
print(n)

from string import punctuation

# text = input('Enter a text: ').split()
# count = 0
# # for c in punctuation:
# #     text = text.replace(c, '')
# article =list(['a', 'an', 'the']) 
# count += article
# print(count)

# list that consists of all palindromic numbers between 100 and 1000.
palindromic_num = [i for i in range(100,1001) if str(i) == str(i)[::-1]]
print(palindromic_num)