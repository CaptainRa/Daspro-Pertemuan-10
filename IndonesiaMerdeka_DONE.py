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

def max2(a,b):
    if a >= b:
        return a
    else :
        return b

def max_list(L):
    if is_empty(L):
        return 0
    else :
        return max2(first(L), max_list(tail(L)))

def IndoMerdeka(L):
    if is_empty(L):
        return 0
    else :
        return (max(first(L)) * 1000000) + IndoMerdeka(tail(L))

print (IndoMerdeka(list_of_list))