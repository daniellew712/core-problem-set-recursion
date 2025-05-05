# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
        
    return n * factorial(n-1)


# reverse

def reverse(text):
    if len(text) <= 1:
        return text
    
    return reverse(text[1:]) + text[0]

# bunny

def bunny(count):
    if count == 0:
        return 0
    return bunny(count-1) + 2

# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif len(parens) % 2 != 0 or parens[0] != '(' or parens[-1] != ')':
        return False
        
    return is_nested_parens(parens[1:-1])