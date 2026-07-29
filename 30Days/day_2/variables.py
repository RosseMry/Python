import keyword

print("\n ======= LEVEL 1 ======= \n")
#Day 2: 30 Days of python programming
first_name = "Rosse"
last_name = "Marcas"
full_name = "Rssemary Marcas"
country = "Peru"
city = "Lima"
age = 28
year = 2026
is_married = True
is_true = 1
is_ligth_on = 1
hello = "world" ; hello2 = "worlds"

print("\n ======= LEVEL 2 ======= \n")
print("Types of variables \n" , type(first_name),"\n",type(last_name),"\n",type(full_name),"\n",type(country),"\n",type(city),"\n",type(age),"\n",type(year),"\n",type(is_married),"\n",type(is_true),"\n",type(is_ligth_on),"\n",type(hello))
print("Len of variable \n", len(first_name))
print("Compare of len \n" , len(first_name) == len(last_name))


# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

print("Results \n", "Addition" , total ,"\n", "diff" ,diff ,"\n","product", product,"\n", "division" , division,"\n", "remainder" , remainder,"\n","exp", exp,"\n","floor Division", floor_division )

'''The radius of a circle is 30 meters.

    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area.'''


radius = int(input('What is the radio : '))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 *( 3.14 * radius)
print("Area of the circle : ", area_of_circle  , "\n Circunference of the circle  : ", circum_of_circle)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_name = str(input('Whats your first name :'))
user_last_name = str(input('Whats your last name :'))
user_country = str(input('From what country are you? : '))
user_age = int(input('How old are you ? :'))
print("User information : ", "\nname ->" , user_name , "\nlast name ->", user_last_name, "\ncountry ->" , user_country, "\nage ->" , user_age)
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print(keyword.kwlist)