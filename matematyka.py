def dodaj(a,b):
    return a+b

def odejmij(a,b):
    return a-b

def pomnoz(a,b):
    return a*b

def podziel(a,b):
    if b==0:
        raise Exception('Dzielnik jest równy zero, dzielenie niemożliwe')
    return a/b

def daj_dodatnie():
    return [1,2,3,4,5,6,7,8,9,-1]