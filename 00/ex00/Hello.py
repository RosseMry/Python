ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"};

#change list by indice
ft_list[1] = "World!";

#tuple are inmutable so cant change create a double
ft_tuple2 = list(ft_tuple);
ft_tuple2[1] = "France!";
ft_tuple = tuple(ft_tuple2);

#set dont have indice need pop and add ? 
ft_set.remove("tutu!");
ft_set.add("Paris!");

#dictionaries acces by keyword
ft_dict["Hello"] = "42Paris!";


#your code here
print(ft_list);
print(ft_tuple);
print(ft_set);
print(ft_dict); 