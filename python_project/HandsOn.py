#Slicing and Variables:

#creating a list 1 to 10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#extract a sublist from my_list only 2 to 5
extract_sublist = my_list[1:5]

#creating a string 'Python is powerful'.
my_string = 'Python is powerful'

#creating a substring from my_string to word 'Python'.
extract_word = my_string[0:6]

#checking if correct
print(extract_sublist, extract_word)

#creating a variable with:
#Full name
full_name = 'Ayala Cohen'
#@-Email
email = 'ayala9490a@gmail.com'
#Age
age = "21"

#printing the variables
print("My name is " + full_name + ", My email is " + email + " and I'm " + age + " years of ages")


#Lists:

#An empty list - my_list
my_list_2 = []

#Adding the elements 1, 2, and 3 to the list
#A option
""""my_list_2.append(1)
my_list_2.append(2)
my_list_2.append(3)"""
#B option
my_list_2.extend([1, 2, 3])

#checking if correct
print(my_list_2)

#Access the second element of the list
print(my_list_2[1])

#Append the element 4 to the list.
my_list_2.append(4)

#Remove the first element from the list
my_list_2.remove(my_list_2[0])

#Print the list in reverse order
my_list_2.reverse()

#Dictionaries:

#Create a dictionary named my_dict with keys 'name', 'age', and 'city'.
my_dict = {
    "name": "Lea",
    "age": "24",
    "city": "Yerushalaim"
}

#Access the value associated with the key 'age'
print(my_dict["age"])

#Add a new key-value pair 'gender': 'Male' to the dictionary.
my_dict["Male"] = "Female"

#Remove the key 'city' from the dictionary.
my_dict.__delitem__("city")

#checking if correct
print(my_dict)

#Check if the key 'name' exists in the dictionary
#I saw some options:
print(my_dict.keys())
print(my_dict.get("name"))
print(my_dict.__contains__("name"))


#Tuples:

#Create a tuple named my_tuple with elements 5, 6, and 7
my_tuple = (5,6,7)


#Access the third element of the tuple.
print(my_tuple[2])

#Concatenate my_tuple with the tuple (8, 9).
my_tuple_2 = my_tuple + (8 ,9)

#checking if correct
print(my_tuple_2)

#Check if the element 6 is present in the tuple.
#return 1 if exist and 0 when doesn't
print(my_tuple_2.count(6))
print(my_tuple_2.__contains__(6))

#Calculate the length of my_tuple
print(my_tuple_2.__len__())

