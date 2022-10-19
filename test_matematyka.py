import pytest
import matematyka

@pytest.mark.podstawy
def test_dodaj():
    assert matematyka.dodaj(1,1)==2

@pytest.mark.podstawy
def test_odejmij():
    assert matematyka.odejmij(4,2)==2

@pytest.mark.zaawansowane
def test_pomnoz():
    assert matematyka.pomnoz(2,3)==6

@pytest.mark.zaawansowane
def test_podziel():
    assert matematyka.podziel(10,5)==2

def test_daj_dodatnie():
    ok=True
    for e in matematyka.daj_dodatnie():
        if e<0:
            ok=False
            raise Exception(f'{e} nie jest dodatnia')
    assert ok