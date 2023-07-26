# WORKING WITH STRINGS
s='convenants'

s=s[:2]+'m'+s[3:]
print(s)
for i in range(len(s)):
    print(s[i])
for i in s:
    print(i)
s=s.upper()
print(s)

s=s.replace('M','N')
print(s)
print(s.count('N'))
print(s.index('N'))
if s[0].isupper():
    print('The first letter is upper')
if s.startswith('C'):
    print('yes')
print("i' am a boy")
print('I\' am a boy')

greet="Hello"
double=''
for c in greet:
    double+=c*2
print(double)
    
from string import punctuation
from math import floor
name=",,ja..;;''m'''e;;s"
for i in punctuation:
    name=name.replace(i, '')
print(name)
print(punctuation)
const='3.14159'
point_index=const.index('.')
print(point_index)
print(const[point_index+1:])

print(float(const)-floor(float(const)))

# ASSIGNMENT ON STRING 1, 2, 3, 5, 7

string_2 = input('Enter a string: ')
sub = string_2
count = 0
count = len(string_2)
print(count)   
print(string_2*10, end=' ') 
print(string_2[0])
print(string_2[0:3])
print(string_2[-3: ])
print(string_2[ : :-1])
# print(string_2[1:-1])
print(string_2.upper())
print(string_2.replace('a','e'))
string_2 = string_2.replace(sub, "____")
print(string_2)

 # A simple way to estimate the number of words in a string is to count the number of spaces in the string. Write a program that asks the user for a string and returns an estimate of how many words are in the string.

_string = input('Enter a string: ')
count = 0
for char in _string:
    if char.isspace():
        count+=1              
print(count +1)
         
    
    
# """ People often forget closing parentheses when entering formulas. Write a program that asks the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses."""
    
# formulas = input('Enter a formula: ')
# count = 0
# for char in formulas:
#     if char =='(':
#         count+=1
#     elif char == ')':
#         count-=1
# if count == 0:
#     print('The',formulas,'has the same number of parentheses')
# else:
#     print('The number of parentheses does not match')
    
# Write a program that asks the user to enter a string. The program should create a new string called new_string from the user’s string such that the second character is changed to an asterisk and three exclamation points are attached to the end of the string. Finally, print new_string. Typical output is shown below:
        # Enter your string: Qbert
        # Q*ert!!! 
        

# myString = input('Enter a string: ')
# for i in range(len(myString)):
#     new_string = myString[:1] + '*' + myString[2:]
#     new_string += '!!!'
# print(new_string)

# Write a program that asks the user to enter a word and determines whether the word is a palindrome or not. A palindrome is a word that reads the same backwards as forwards.

# palindrome = input('Enter a word: ')
# if palindrome[ : :-1] == palindrome:
#     print(palindrome,'is a panlindrome')
# else:
#     print('not a palindrome')
   