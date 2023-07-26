# NESTED LOOPS
# Print a 10 × 10 multiplication table.
from string  import punctuation
for i in range(1,11):
    for j in range(1,11):
        print('{:3d}'.format(i*j), end=' ')
    print()
    

for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            if x**2 + y**2 == z**2:
                for i in range(2,x):
                    if x%i == 0 and y%i==0 and z%i==0:
                        break
                else:
                    print((x,y,z), end=' ')
                    
                    
                    
D={'A':500, 'B':800}
D['C']=899

print(D)
print(D['A'])
del D['B']
D.pop('A')
print(D)


points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}


word='jagons'
word=word.upper()
word_points=sum([points[c] for c in word] )
print('Your points is ', word_points)

# for key in points:
#     print(points[key], end=" ")
    
for val in points.items():
    print(val)
list_points=list(points.items())
print(list_points)
print(dict(list_points))
# ################

text=open('./WEEK3/content.txt').read()
print(text)

for i in punctuation:
    text=text.replace(i, '')
text=text.lower()

words=text.split()
print(words)

d={}
for w in words:
    if w in d:
        d[w]=d[w]+1
    else:
        d[w]=1

items=list(d.items())
items.sort()
for item in items:
    print(item)

# days = {'January':31, 'February':28, 'March':31, 'April':30,
# 'May':31, 'June':30, 'July':31, 'August':31,
# 'September':30, 'October':31, 'November':30, 'December':31}

# entry = input('enter a month: ')
# entry = entry.capitalize()
# sort_days = sorted(days)
# days_31 = [i[0] for i in days.items() if i[1] == 31]
# sort_key = list(days.values())
# sort_key.sort()
# print('There are days', days[entry])
# print(sort_days)
# print(days_31)
# print(list(days.items()))
# print(sort_key)

# scores = {}
# num_team = eval(input('enter number of teams: '))
# for i in range(num_team):
#     team_name = input('enter a team name: ')
#     game_won = eval(input('how many game team won: '))
#     game_lose = eval(input('how many game team lost: '))
#     scores[team_name] = [game_won,game_lose]
# print(scores)

# name = input('enter a team name: ')
# percentage = (scores[name][0]/sum(scores[name])*100)
# print('Winning percentage of team', name,'is', percentage,'%')

# win_team = [i[0] for  i in scores.values()]
# print(win_team)

# win_record = []
# for i in scores:
#     if scores[i][0] > 0:
#         win_record.append(i)
# print(win_record)


l = {}