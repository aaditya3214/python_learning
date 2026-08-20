# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

my_dict = {
    "angoor" : "Grapes",
    "papita" : "Papaya",
    "kela" : "Banana",
    "aam" : "Mango"
}
word = input("Enter word you want to know English meaning: ")
print(my_dict[word])
print(type(my_dict))