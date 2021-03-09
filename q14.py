'''
Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
'''

def read_csv():
    import csv

    csvfile = open('name.csv','r',newline='')
    obj = csv.DictReader(csvfile)
    for row in obj:
        print(row)

read_csv()