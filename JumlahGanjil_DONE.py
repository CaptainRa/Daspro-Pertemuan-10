import ast
list = ast.literal_eval(input())

def is_empty(L):
    return L == []

def first(L):
    return L[0]

def tail(L):
    return L[1:]

def is_atom(L):
    return len(str(L))==1

def is_list(L):
    return not (is_atom(L))

def jml_ganjil(L):
    if is_empty(L):
        return 0
    else:
        if is_list(first(L)):
            return jml_ganjil(first(L)) + jml_ganjil(tail(L))
        else :
            if first(L) % 2 == 1:
                return first(L) + jml_ganjil(tail(L))
            else :
                return 0 + jml_ganjil(tail(L)) 

print(jml_ganjil(list))