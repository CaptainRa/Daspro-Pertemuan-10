import ast
list_of_list = ast.literal_eval(input())

def is_empty(L):
    return L == []

def first(L):
    return L[0]

def tail(L):
    return L[1:]

def is_atom(L):
    return len(str(L)) == 1

def is_list(L):
    return not (is_atom(L))

def is_prima (n, i = 2):
    if (n < 2):
        return False
    elif (n == 2):
        return True
    elif (n % i == 0):
        return False
    elif (i * i > n):
        return True
    else :
        return is_prima (n, i + 1)

def jml_prima(L):
    if is_empty(L):
        return 0
    elif is_list(first(L)):
        return jml_prima(first(L)) + jml_prima(tail(L))
    else :
        if is_prima(first(L)):
            return first(L) + jml_prima(tail(L))
        else :
            return 0 + jml_prima(tail(L))

print (jml_prima(list_of_list))