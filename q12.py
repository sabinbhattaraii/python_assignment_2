'''
Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed
'''

def is_palindrome(string):
    string = string.lower()
    if list(string) == list(reversed(string)):
        return 'The word is palindrome'
    else:
        return 'The word is not palindrome' 

string = str(input('Enter a word :'))
print(is_palindrome(string))