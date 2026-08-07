print("\n====== DICTIONARY =======\n")
dict = {}
dog = {'name':'Bryan', 'color':'marron', 'breed':'quoi', 'legs':4, 'age':50}
student = {'first_name' : 'Marlon', 'last_name' : 'Sandoval', 'gender' : 'Fem', 'age' : 25, 'marital status' : 'single', 
           'skills' : ['Dance', 'kung fu', 'Autocad'], 'country' : 'New Zeland', 'city' : 'Tokyo' , 'address' :'Mariscal Jose de San martin 123'}
print('1.Empty dictionary :', dict)
print('2. Dog dictionary :', dog)
print(f'3. Student len {len(student)} and values : {student}'  f'\n Value of skills : {student["skills"]} \n y su datatype {type(student['skills'])}')
student['skills'].append('HTML')
student['skills'].append('cOOKING')
print(f'7. Get the keys as a list : {student.keys()}')
print(f'8. Get the values as a list : {student.values()}')
students = student.items()
del student['country']
print(f'10. Delete a item of dictionary : {student}')
del student

