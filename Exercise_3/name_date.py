letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name = input("Enter your first name here:")
date = input("Enter selected date here:")

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)