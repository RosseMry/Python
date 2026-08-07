it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("\n====== SET =======\n")
print('1, Len of set', len(it_companies))
it_companies.add('Twiter')
print('2. Add a item', it_companies)
it_companies.update(['hulu', 'NVidia', 'Samsung'])
print('3. Adding with update :' , it_companies)
it_companies.pop()
print('4. Removing a random company', it_companies)
#when u discard and dont have the item u will not notice with remove it pop an error when it dont find the item

print("\n====== LEVEL 2 =======\n")
C = A | B
print(f'1. Joning A and B {C}')
C = A.intersection(B)
print(f'2.Interseccion de A and B : {C}')
print(f' is A a subset de B ? :{ A.issubset(B)} , are A and B disjoint ? : {A.isdisjoint(B)}')
print(f'5. Joinf of A and B : {A.union(B)}')
print(f'6. Join B with A : {B.union(A)}')
print(f'7. Symetric Difference : {A.symmetric_difference(B)}')
del A
del B
del it_companies

print("\n====== LEVEL 3 =======\n")
age_set = set(age)
print(f'1.Len of the list = {len(age)} , len of set = {len(age_set)}')
str= 'I am a teacher and I love to inspire and teach people'
words = set(str.split())
print('3. Converting a str to list with slipt and this to set to remove dups' , words)

