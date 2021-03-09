'''
​ Write a Python class to find the three elements that sum to zero​ ​ froma list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
'''

class Zero:

    def check(self, my_list):
        list1 = []
        result= []
        for i in range(0, len(my_list)-2):
            for j in range(i+1, len(my_list)-1):
                for k in range(j+1, len(my_list)):
                    if my_list[i] + my_list[j] + my_list[k] == 0:
                        list1 = [my_list[i], my_list[j], my_list[k]]
                        result.append(list1)
        print(result)

X = Zero()
X.check([-25, -10, -7, -3, 2, 4, 8, 10])