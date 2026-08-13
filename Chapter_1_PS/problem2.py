import os

# 1. Get the path from the user
user_path = input("Enter the path: ")

# 2. Get the contents of the folder
contents = os.listdir(user_path)

# 3. Print each item one by one
for item in contents:
    print(item)