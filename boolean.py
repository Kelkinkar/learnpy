age  = int(input('Enter your age: '))
less_age = age < 18
pass_age = age >= 18
print(f" Are you are of age: {pass_age}")

""" and operator returns the first operator if its false or else returns the second value
while or operator returns the first value if its true or else it returns the second value
"""
f_name = input('Enter your first name: ')
sur_name = input('Enter your surname: ')
identity = f_name or sur_name
print(identity)