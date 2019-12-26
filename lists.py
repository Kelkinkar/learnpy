# printing out the methods associated with a lists
y = []
a = dir(y)
for b in a:
	print(b)
# using some of the methods
k = ['Kelvin', 'John', 'Simon', 'Peter', 'Ngone', 'Aleki', 'Maina', 'Kimani']
num = [45, 67, 56, 89, 1000, 32, 89, 345, 56]
	#using append method


k.append('Faith')
print(k)

	#using pop method
	   #by default, pop removes objects from the end of string but you can specify index wise


k.pop()
print(k)
k.pop(1)
print(k)
	# remove method

k.remove('Kelvin')
print(k)

""" with remove, you have to specify the object you want to omit but with pop, you just 
	need the index"""

	#sort method

num.sort() # its an in place method so you cant directly assign it a value i.e sort_list = num.sort()
sort_list = num
print(sort_list)

# count method - this method calculates how many times an object appears in a list
d = num.count(56)
print(d)

#insert method - species a certain index to insert an object in the list
num.insert(4, 3) #first value is the index and the second value is the object
print(num)

#extend method - joins a list to another list
num.extend(k)
print(num)

#index method - species the first occurrence of an object in a list
b = num.index(56, 3) # 3 species the index to begin at
print(b)

# reverse method - just as the name, it reverses the objects in a string
num.reverse()
print(num)



# sort mwthod takes a key and a reverse flag
num1 = [34, 79098, 848, 736, 737, 6325, 546]
num1.sort(reverse = True)
srt = num1
print(srt)

#because  sort is an in place method, you can use sorted method to directly print out the sorted value
sorted(num1)
print(num1)

#copy method - creates a shallow copy
num1.copy()
print(num1)

#clear method - clears all objects in a list


#.join is used to print out objects of a list into a string. The objects must be a string.
str_separator = ", ".join(k)
congrats = f"My friends are as follows :{str_separator}"
print(congrats)

num2 = [5345, 939, 9239, 535, 6367]
v = str(num2)
print(v)
str_separator = " & ".join(v)
congrats = f"My grades are as follows :{str_separator}"
print(congrats)
