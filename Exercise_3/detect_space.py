name = "Sita  Ram"

print(name)

space_detect = name.count(" ")

print(space_detect) # it returns 2


# replace double space with single space 

name = name.replace("  ", " ")

space_detect = name.count(" ")

print(space_detect) # it returns 1 here 

print(name)