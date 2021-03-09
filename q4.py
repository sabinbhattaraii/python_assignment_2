'''
Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
'''

lists = []
n = int(input("Enter how may names you enter:"))
for i in range(0,n):
    name = input("Enter names of your colleagues and friends:")
    lists.append(name)
lists.sort()
print(f"The first item in the list is {lists[0]}")
print(f"The second item in the list is {lists[1]}")