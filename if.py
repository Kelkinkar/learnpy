friend = ["Kelvin", "Ngone", "Mukurino", "Aleki"]
family = ["Julie", "Kennedy", "Sammy"]

name = input("What is your name: ")

if name in friend:
	print(f"Hello {name}, you are my friend")
elif name in family:
	print(f"Hello {name}, you are family")
else:
	print("you should know people")

