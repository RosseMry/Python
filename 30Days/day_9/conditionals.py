print("\n====== CONDITIONALS =======\n")
age = int(input('Enter your age : '))

if age < 18 :
    print(f'You need {18 - age} more years to learn to drive.')
else:
    print('You are old enough to drive.\n')


print ("Whos's older?")
age = int(input('Enter your age: '))
mine = 28
if age < mine :
    print(f'You are {mine - age} years younger than me.')
else :   
    print(f'You are {age - mine} years older than me.')

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
if a > b :
    print('a is greater than b')
elif a < b :
    print(' a is smaller than b')
else : 
    print(' a equal b')

print("\n====== LEVEL 2 =======\n")

grade = input('Isert grade :')
if grade > 90 and grade <= 100 :
    print('A')
elif grade >= 80 and grade <=89:
    print('B')
elif grade >= 70 and grade <= 79:
    print('C')
elif grade >= 60 and grade <= 69:
    print('D')
elif grade >= 0 and grade <= 59:
    print('F')

Autumn = ['September', 'October', 'November'] 
Winter = ['December', 'January' ,'February'] 
Spring = ['March,', 'April', 'May']
Summer = ['June', 'July', 'August']

month = str(input('Whats ur month ? :')).capitalize() #para que sea str y este capitalizado c: 
if month in Autumn :
    print('The season is Autumn')
elif month in Winter :
    print('The season is Winter')
elif month in Spring :
    print('The season is Spring')
elif month in Summer :
    print('The season is Summer')
else :
    print('Invalid Month')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('Insert your fruit :')).lower()

if (fruit in fruits) != 1 :
    fruits.append(fruit)
    print('New list :', fruits)
else:
    print('Fruit already in the list ')

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_married': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}


if person['skills'] :
    print('The middle skill is :', person['skills'][len(person['skills']) // 2])
else: 
    print('Dont have skills like key')

if person['skills']:
    print('2. Have python like skill ? ', 'Python' in person['skills'])

skills2 = set(person['skills'])
if skills2 == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'} <= skills2:
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'} <= skills2:
    print('He is a fullstack developer')
else:
    print('unknown title')

if person['is_married'] == True and person['country'] == 'Finland' :
    print(f'{person['first_name']} {person['last_name']} lives in {person["country"]}. He is married')