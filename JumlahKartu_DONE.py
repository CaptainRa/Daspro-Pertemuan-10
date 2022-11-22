import ast
list_of_list = ast.literal_eval(input())

def is_empty_LoL(L):
    return L == []

def is_atom(L):
    return len(str(L)) == 1

def is_list(L):
    return not is_atom(L)

def first_list(L):
    return L[0]

def tail_list(L):
    return L[1:]

def jumlah(L):
    if is_empty_LoL(L):
        return 0
    else :
        if is_list(first_list(L)):
            return jumlah(first_list(L)) + jumlah(tail_list(L))
        else : 
            return 1 + jumlah(tail_list(L))

print (jumlah(list_of_list))