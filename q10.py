'''
Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well
'''

def snake_case(string, separator):
    change = [string[0].lower()]
    for i in string[1:]:
        if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            change.append('_')
            change.append(i.lower())
        else:
            change.append(i)
    snake = ''.join(change)
    kebab = separator.join(snake).lower()
    return snake,kebab


string = str(input('Enter a string in Camel-case'))
print(snake_case(string,'-'))

