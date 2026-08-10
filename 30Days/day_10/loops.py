from countries import countriese
from countries import countries

print("\n====== LOOPS =======\n")

'''for i in range(11): print(i);

i = 0
while i < 11 : 
    print(i)
    i = i+1 

for i in range(10,0,-1) : print(i)

i = 10
while i > 0 :
    print(i)
    i = i-1 


for i in range(0,7):
    for y in range(i):
        print('*', end = '')
    print()

for i in range(0, 8):
    for y in range(8):
        print('# ', end = '')
    print()

y = 0
for i in range(11) :
    print(f'{i} x {y} = {i * y}')
    y = y+1

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i) 

for i in range(100):
    if i % 2 == 0 and i != 0:
        print(i) 

for i in range(100):
    if i % 2 != 0 :
        print(i) 

print("\n====== LEVEL 2 =======\n")

sum = 0
for i in range(101):
    sum = sum + i
print('The sum of all numbers is ',sum)

sum_even = 0
sum_odd = 0

for i in range(101) :
    if i % 2 == 0 and i != 0 :
        sum_even = sum_even + i
    else :
        sum_odd = sum_odd + i;

print(f'The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.')
'''

countries2 = [country for country in countries if "land" in country ]
print (countries2)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_rev = [fruit for fruit in fruits[::-1]]
print(fruit_rev)

languages = [country['languages'] for country in countriese]
st = set(idiom for idiom in languages)
print(f'Total of languages {len(languages)}')

