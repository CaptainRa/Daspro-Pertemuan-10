import ast
list_of_list = ast.literal_eval(input())
kelipatan = int(input())

def is_empty(L):
    return L ==[]

def is_atom(L):
    return len(str(L)) == 1

def is_list(L):
    return not (is_atom(L))

def first(L):
    return L[0]

def tail(L):
    return L[1:]

def konso_LoL(s,L):
    if is_empty(L):
        return [s]
    else :
        return [s] + L

def rember(a,L):
    if is_empty(L):
        return L
    else :
        if is_list(first(L)):
            return konso_LoL(rember(a,first(L)),rember(a,tail(L)))
        else :
            if first(L) == a:
                return rember(a,tail(L))
            else :
                return konso_LoL(first(L), rember(a,tail(L)))

def monster(a,L):
    if is_empty(L):
        return L
    else :
        if is_list(first(L)):
            return konso_LoL(monster(a,first(L)), monster(a,tail(L)))
        else :
            if first(L) % a == 0:
                return monster(a,rember(a,tail(L)))
            else :
                return konso_LoL(first(L), monster(a,tail(L)))


print (monster(kelipatan, list_of_list))