"""we use input() funtion to get input from the user. Takes evrything to be a string and you have to use int()
   function to use integers."""

name = input('What is your name? : ')
age = int(input('What is your age? : '))
if age <= 25:
	print(f'hello {name}, you are age {age} hence you cannot access this service. Try to access gurukids and sing babyshark')
elif age >= 26 and age <= 30:
	print(f'hello {name}, you are of age motherfucker.. enjoy while it lasts')
elif age >31:
	print(f'hello {name}, you are too old to access this service, go make some kids ')
