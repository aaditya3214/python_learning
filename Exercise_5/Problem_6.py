# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

language = {

}
print(language, type(language)) 

name1 = input("Enter your first name here: ")
lang1 = input("Enter your favorite programming language: ")
language.update({name1 : lang1})

name2 = input("Enter your first name here: ")
lang2 = input("Enter your favorite programming language: ")
language.update({name2 : lang2})

name3 = input("Enter your first name here: ")
lang3 = input("Enter your favorite programming language: ")
language.update({name3 : lang3})


name4 = input("Enter your first name here: ")
lang4 = input("Enter your favorite programming language: ")
language.update({name4 : lang4})


print(language, type(language))
print(name1, name2, name3, name4)
print(lang1, lang2, lang3, lang4)


# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

# Update

# 8. If languages of two friends are same; what will happen to the program in problem 6?

# nothing 





