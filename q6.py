'''
Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
'''

lists = input("Enter name of friends and collegues").split(' ')
print(lists)
for i in lists:
    if i.lower() == 'john':
        print('John found')
        break
else:
    print("John not found")

