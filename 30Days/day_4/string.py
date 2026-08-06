print("\n====== CONCATENATION =======\n")
string = 'Thirty' +' ' +'Days' + ' ' + 'Of' + ' ' + 'Python'
print(string)

string = 'Coding ' +' ' + 'For ' +' ' + 'All'
print(string)

print("\n====== UPER  LOWER CAPITALIZE  =======\n")
company = 'Coding For All'
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])


print(company.find('Coding')) #-1 false , index 4 true
print(company.replace('Coding', 'Flexing'))
company2 = company.replace('Coding', 'Python').replace('All', 'Everyone')

print("\n====== SPLIT  =======\n")
print(company2)
print(company2.split())
catorce = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(catorce.split(','))
print("15.Character at index 0 : ", company[0])
print("16.Character at last index : ", company[-1])
print("17.Character at index 10 : ", company[10])


print("\n====== ACRONYM =======\n")
company = 'Coding For All'
companys = company.split(" ")
acro = ""
for i in companys:
    if i:
        acro+=i[0].upper()
        
print(acro) 
print(companys)

python2 = 'Python For Everyone'
python3 = python2.split()
acro2 = ""
print(python3, "the acronym is ")
for i in python3:
    if i:
        acro2 += i[0]

print(acro2)

code = 'Coding For All'
c_str = 'C'
F_str = 'F'
I_str = 'I'
print(code.index(c_str))
print(code.index('F'))
#print(code.rindex(I_str))

sentence ='You cannot end a sentence with because because because is a conjunction'
sub_str = 'because'
print(sentence.index(sub_str))
print(sentence.rindex(sub_str))

print(code.startswith('Coding'))
print(code.endswith('Coding'))
code = '   Coding For All      '
print(code.strip("  "))
#isidentifier check is a string is a valid variable name / dont start with number etc
types =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(types))
#faltan 3
sentence = "I am enjoying this challenge. \n I just wonder what is next."
print(sentence.split('\n'))
sentence = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(sentence)

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
