print("\n====== LIST =======\n")
lst = []
lst = ['itm1', 'itm2', 'imt3', 30, 50]
print("finding len of list", len(lst))
print(f"Print items the first {lst[0]} the middle {lst[3]} the last {lst[len(lst)-1]}")

mixed_data_types = ['Rosse', 28, 1,57, 'Divoce', '2 rude de moulins']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(it_companies)
print(len(it_companies))
print(f"First company in list {it_companies[0]} middle company {it_companies[3]} las company{it_companies[len(it_companies)-1]}")
it_companies[3] = 'Tesla'
print(it_companies)
it_companies.append('NVidia')
print(it_companies)
it_companies.insert(4,'Intel')
print("12. After insert : ", it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)
print('#; '.join(it_companies))
print(f'15. Exist Meta in it_companies : {'Meta' in it_companies}')
it_companies.sort() #primero sort luego imprimir
print('16. Sorting the list: ', it_companies)
it_companies.reverse()
print('17. Reversing list :', it_companies)
