'''
Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
'''

def binary_search(array,index):
    for i in range(len(array)):
        if index in array:
            return array.index(index)
        else:
            return -1

array = [1,2,3,4,5,6,7,8,9,10]
number = int(input("Enter the number to find:"))
print(binary_search(array,number))