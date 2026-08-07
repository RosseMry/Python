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
first_three = it_companies[0:3]
print('18. first three companies :', first_three)
last_three = it_companies[-3::] #from -3 to the end
print('19. Last three companies:', last_three)
middle_company = it_companies[len(it_companies)//2]
print('20. Middle company:', middle_company)
print('21. pop 1 :', it_companies.pop(0))
print('22. pop middle :', it_companies.pop(len(it_companies)//2))
print('23. pop last :', it_companies.pop())
print('24. clear all :',it_companies.clear())
del it_companies #Destroy the IT companies list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

print("\n====== Exercises: Level 2 =======\n")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
age_min = ages[0]
age_max= ages[len(ages)- 1]
mean_age = (ages[len(ages)//2] + ages[len(ages)//2 + 1]) / 2
print('Sorting ages', ages)
print(f'Min {age_min} and Max {age_max}')
print(f'Mean age is : {mean_age}')
range_ages = age_max - age_min
print(f'range age is {range_ages}')


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
print('1. Find the middle country : ', countries[len(countries)//2])
slice1 = countries[0:(len(countries)//2)]
slice2 = countries[(len(countries)//2):-1]
print('nros : ',len(slice1), len(slice2))
