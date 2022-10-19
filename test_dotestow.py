import dotestow
def test_liczby_ilosc():
    assert len(dotestow.liczby())==100

# def test_liczby_zakres():
#     liczby=dotestow.liczby()
#     assert min(liczby)>0
#     assert max(liczby)<=100

def test_liczby_zakres():
    ok=True
    for e in dotestow.liczby():
        if e<1 or e>100:
            ok=False
            raise Exception(f'liczba {e} poza zakresem')
    assert ok

def test_liczby_typ():
    ok=True
    for e in dotestow.liczby():
        if type(e) is not int:
            ok=False
            raise Exception(f'element {e} nie jest liczbą całkowitą')
    assert ok