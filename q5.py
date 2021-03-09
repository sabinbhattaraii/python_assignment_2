'''
Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age
'''


lists = []
tuple1 = ('Ram','Bahadur',20)
lists.append(tuple1)
tuple2 = ('Hari','Gurung',27)
tuple3 = ('Shyam','Rai',50)
tuple4 = ('Gokul','Neupana',12)
lists.append(tuple2)
lists.append(tuple3)
lists.append(tuple4)
sorted_by = sorted(lists,key=lambda tup: tup[1])

print(lists)
print(sorted_by)