"""Sets are very useful in python and are different from tuples and lists in that you can get the difference in elements
from one set to another"""

x = {}
y = dir(x)
for b in y:
	print(b, '\n')

java_class = {'Kelvin', 'Jane', 'Henry' , 'Simon', 'Anne', 'Joseph'}
python_class = {'Kelvin', 'Simon', 'Sammy', 'Yussuf', 'Ahmed'}

#diff method gets the elements which are in set A and are not in set B
diff = java_class.difference(python_class)
print(diff)

#sym diff method gets the elements that are not in both sets
sym_diff = java_class.symmetric_difference(python_class)
print(sym_diff)

#intersection method gets the elements that are in both sets
inter = java_class.intersection(python_class)
print(inter)

#union method combines both of the lists
un  =java_class.union(python_class)
print(un)
