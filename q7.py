'''
Create a list of tuples of first name, last name, and age for your friends
and colleagues. If you don't know the age, put in None. Calculate the
average age, skipping over any None values. Print out each name,
followed by old or young if they are above or below the average age.
'''

my_list = [('Ram', 'Bahadur', 40), ('Shyam', 'Bahadur', 30), ('Hari', 'Bahadur', 25)]
age = []
for i in range(len(my_list)):
    age.append(my_list[i][2])
print(age)
avg = sum(age)/len(age)
print(f"The average age is: {avg}")

for i in range(len(my_list)):
    if my_list[i][2] > avg:
        print(my_list[i][0] + " is old")
    else:
        print(my_list[i][0] + " is young")