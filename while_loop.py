"""While loop is used to repeat an object for undefined number of times. Its the user who decides
when to stop the program"""
"""For loop is use to repeat something for a definate number of times"""
a  = input("Do you want to play a game?(yes/no): ")
while a == "yes":

	x = int(input("Enter a number between 0 and 9: "))
	y = int(input("Enter another number between 0 and 9: "))	
	print(f"Multiply your number{x} and number {y}")
	z = x * y
	print(f"Add the result of your two numbers {z}")
	print("Congratulations you have a number between 0 and 10")
	a  = input("Do you want to play a game?(yes/no): ")
print("Exit with code 0")