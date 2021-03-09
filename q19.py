'''
Write a Python class to find validity of a string of parentheses, '(', ​ ')',
'{', '}', '[' and ']. These brackets must be close in the correct order, ​ for
example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
'''

class Validity:

    def is_valid(self,string):
        lists, dict1 = [], {"(": ")", "{": "}", "[": "]"}
        for p in string:
            if p in dict1:
                lists.append(p)
            elif len(lists) == 0 or dict1[lists.pop()] is not p:
                return False
        return len(lists) == 0


print(Validity().is_valid("()"))
print(Validity().is_valid("[)"))
print(Validity().is_valid("{{}}"))