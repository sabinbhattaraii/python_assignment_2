'''
Write a function, is_prime, that takes an integer and returns True if the
number is prime and False if the number is not prime.
'''

def is_prime(integer):
    lists = []
    if integer >= 1:
        for i in range(2,integer):
            if integer % i ==0:
                return False
                break
        else:
            return True
    else:
        return False


integer = int(input("Enter a number"))
print(is_prime(integer))