import ast
list_of_list = ast.literal_eval(input())

def is_empty(L):
    return L == []

def first(L):
    return L[0]

def tail(L):
    return L[1:]

def last(L):
    return L[-1]

def head(L):
    return L[0:-1]

def is_atom(L):
    return len(str(L)) == 1

def is_list(L):
    return not (is_atom(L))

def jumlah(L):
    if is_empty(L):
        return 0
    else :
        return first(L) + jumlah(tail(L))

def permen(L):
    if is_empty(L):
        return 0
    else :
        if is_list(first(L)):
            if jumlah(first(L)) % 2 == 1:
                return (jumlah(first(L)) * 1000) + (permen(tail(L)))
            else :
                return (jumlah(first(L)) * 2000) + (permen(tail(L)))
        else :
            if first(L) % 2 == 0:
                return (first(L) * 4000) + (permen(tail(L)))
            else :
                return (first(L) * 3000) + (permen(tail(L)))

print (permen(list_of_list))