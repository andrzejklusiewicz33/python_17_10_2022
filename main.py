# test
# Andrzej Klusiewicz
# print("Hello world")
# print('Hello world')
# print("Hello world in Mc'Donalds")
# zmienna='Kot'
# zmienna2=1234
# print(zmienna2)
# print(type(zmienna2))
# print("zmienna="+zmienna+"!")
# #print('zmienna2='+zmienna2)
# print('zmienna2='+str(zmienna2))
# x=123
# y=456
# print(x,y)
# print("x="+str(x)+" y="+str(y))
# print("x={} y={}".format(x,y))
# print(f"x={x} y={y}")
# print(f'x={x} y={y}')

# owoc=input('Podaj nazwę owocu:')
# print(f'Wybrany owoc to {owoc}')

#
# owoc=input('Podaj nazwę owocu:\n')
# print(f'Wybrany owoc to {owoc}')


# 1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
#
# first_name=input('Podaj imię:\n')
# last_name=input('Podaj nazwisko:\n')
# print(f'Witaj {first_name} {last_name}!')
# print("Witaj "+first_name+' '+last_name+'!')
# print("Witaj {} {}!".format(first_name,last_name))
#
# liczba=input('podaj liczbę:\n')
# print(liczba,type(liczba))
# print(liczba/2)

# print('xyz'*10)


#
# liczba=float(input('podaj liczbę:\n'))
# print(liczba,type(liczba))
# print(liczba/2)

#
#
# liczba=int(input('podaj liczbę:\n'))
# print(liczba,type(liczba))
# print(liczba/2)

# 2. • BMI= masa/(wzrost*wzrost) .
# Napisz program który odbierze od użytkownika jego masę w kilogramach i wzrost w metrach,
# wyliczy i wypisze BMI.

# print(pow(1.76,2))
#
# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# bmi=round(masa/pow(wzrost,2),2)
# print(f"bmi={bmi}")

# przerwa do 10:31


# x=-9
# if x>0:
#     print('x jest większe od 0')
#     print('x jest większe od 0')
#     print('x jest większe od 0')
# print('koniec')
#
# x=9
# if x==1:
#     print('x jest równe jeden')
# elif x==2:
#     print('x jest równe dwa')
# elif x==3:
#     print('x jest równe trzy')
# else:
#     print('poza zakresem')

# 3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość z informacją "wartość dodatnia",
# jeśli zero to wyświetlamy z informacją "równe zero", jeśli ujemna to wyświetlamy "wartość ujemna".

# x=int(input('podaj liczbę:\n'))
# if x>0:
#     print(f'x={x} jest dodatni')
# elif x==0:
#     print(f'x={x} jest równy zero')
# else:
#     print(f'x={x} jest ujemny')


# 4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
# wyświetlił nam również odpowiedni opis wg skali z Wikipedii.
#
# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# bmi=round(masa/pow(wzrost,2),2)
# print(f"bmi={bmi}")
# if bmi<16:
#     print('wyglodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('pożądana masa ciała')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('otyłość 1 stopnia')
# elif bmi<40:
#     print('otyłość 2 stopnia')
# else:
#     print('otyłość 3 stopnia')
#
# for x in range(10):
#     print(x)

#
# for x in range(1,11):
#     print(x)
#


# for x in range(1,11,2):
#     print(x)


#
# for x in range(1,11):
#     print(x)

# help(range)
#
# for x in range(1,11):
#     print(x)
# print('koniec')

# 5. Wyświetl 20 kolejnych potęg liczby 2
#
# for p in range(1,21):
#     print(f"2^{p}={pow(2,p)}")


# for p in range(1,21): print(f"2^{p}={pow(2,p)}")
#
# for p in range(1,21):
#     print(f"2^{p}={pow(2,p)}")
#     if 1==1:
#         pass


# 6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
# parzysta czy nieparzysta
#
# print(11%2)
#
# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} jest parzyste')
#     else:
#         print(f'{x} jest nieparzyste')

# for x in range(-10,11):
#     if x==0:
#         continue
#     print(x)
#
# for x in range(-10,11):
#     if x==0:
#         break
#     print(x)

# 7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakladamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
# Kapitalizacja comiesięczna
#
# hajs=1000000
# oprocentowanie=0.03
# ilosc_miesiecy=24
# for m in range(1,ilosc_miesiecy+1):
#     hajs=round(hajs+(hajs*oprocentowanie/12),2)
#     print(m,hajs)

# while True:
#     pass
#
# while 1==1:
#     print("1==1")
#
# x=1
# while x<1000:
#     x=x*2
#     print(x)

# 8. Napisz korzystajac z petli while program który wyświetli
#   10 kolejnych potęg liczby 2.
#
# p=1
# while p<=10:
#     print(p,pow(2,p))
#     p += 1
#     #p=p+1
#

# 9. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość  potęgi
# nie przekroczy wartości podanej przez użytkownika
#
# max=int(input('podaj maksymalną wartość:\n'))
# potega=0
# np=0
# while potega<=max:
#     np+=1
#     potega=pow(2,np)
#     print(potega)

# 10. Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od wartosci podanej przez uzytkownika

# import random
# print(random.randint(1,100))

# import random
# max=int(input('podaj max zakres:\n'))
# suma=0
# while suma<=max:
#     suma+=random.randint(1,10)
#     print(f'suma={suma}')


# przerwa do 11:41
#
# tekst="\n             siała BABA mak, dostała 10 lat bo nie płaciła VAT       "
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.title())
# print(tekst.replace('a','X'))
# print(tekst.replace('a','X').replace('A','X'))
# print(tekst.lower().replace('a','X'))
# print(len(tekst))
# lista=[1,2,3]
# print(len(lista))
# print(tekst.count('a'))
# print(tekst.lower().count('a'))
# print(tekst.strip())
# print(tekst.split())
# linia='1;Andrzej;Klusiewicz'
# print(linia.split(';'))

# 11. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z niego znaki ,.!?
# i wyświetli powiększony do dużych liter na konsoli

# odebrane=input('podaj tekst:\n')
# print(odebrane.upper().replace(',','').replace('.','').replace('!','').replace('?',''))

# tekst="siała BABA mak, dostała 10 lat bo nie płaciła VAT"
#
# if 'baba' in tekst.lower():
#     print('jest baba')
# else:
#     print('nie ma baby')
#
# plik=open('tadzio.txt',encoding='utf-8')
# for linia in plik:
#     print(linia)
#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(linia)
#
# with open('tadzio.txt',encoding='utf-8') as plik:
#     for linia in plik:
#         print(linia)

#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia.strip()),linia.strip())

# 12. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik

# nazwa_pliku=input('podaj nazwę pliku:\n')
# for linia in open(nazwa_pliku,encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(linia.strip())
#
# calosc=open('tadzio.txt',encoding='utf-8').read()
# print(calosc)
# print(calosc.count('a'))

# 13. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego
# podanego przez użytkownika w pliku którego nazwę również poda użytkownik.

# szukane=input('podaj szukane:\n')
# nazwa_pliku=input('podaj nazwę pliku:\n')
# print(  open(nazwa_pliku,encoding='utf-8').read().lower().count( szukane.lower()  )  )


# print(  open(input('podaj nazwę pliku:\n'),encoding='utf-8').read().lower().count( input('podaj szukane:\n').lower()  )  )
# print('siema')
#
# szukane=input('podaj szukane:\n')
# nazwa_pliku=input('podaj nazwę pliku:\n')
# plik=open(nazwa_pliku,encoding='utf-8')
# calosc=plik.read()
# pomniejszona_calosc=calosc.lower()
# pomniejszone_szukane=szukane.lower()
# print(pomniejszona_calosc.count(pomniejszone_szukane))
#
# szukane=input('podaj szukane:\n').lower()
# nazwa_pliku=input('podaj nazwę pliku:\n')
# calosc=open(nazwa_pliku,encoding='utf-8').read().lower()
# print(  calosc.count( szukane  )  )

# 14. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
#  po  odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
#  i w  jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.
#
# szukane=input('podaj poszukiwaną frazę:\n')
# nazwa_pliku=input('podaj nazwę pliku:\n')
# x=0
# for linia in open(nazwa_pliku,encoding='utf-8'):
#      x+=1
#      if szukane.lower() in linia.lower():
#         print(x,linia.strip())
#
# tekst="siała baba mak, dostała 10 lat bo nie płaciła VAT"
# print(tekst[0])
# print(tekst[0:10])
# print(tekst[0:10:2])

# 15. Napisz program który będzie od uzytkownika przyjmowal nazwę pliku z kodem pythona.
# Program ma wyświetlić wszystkie linie które nie są w całości komentarzami wraz z numerami tych linii w pliku
#
# #komentarz
# print('siema to ja') #komentarz
#                     #komentarz

# nazwa_pliku=input('podaj nazwę pliku:\n')
# for linia in open(nazwa_pliku,encoding='utf-8'):
#     if len(linia.strip())>0 and linia.strip()[0]!='#':
#         print(linia.strip())
#
# nazwa_pliku=input('podaj nazwę pliku:\n')
# for linia in open(nazwa_pliku,encoding='utf-8'):
#     if  linia.strip()[0]!='#' and len(linia.strip())>0: #fuuuuu
#         print(linia.strip())

# przerwa do 13:00

# listy, krotki, słowniki, zestawy
#
# lista=[]
# lista=list()
# lista=[1,2,3,4]
# print(lista,type(lista))
# lista.append(5)
# lista.append(6)
# for element in lista:
#     print(element)

# 16. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
#
# lista=[]
# for p in range(1,11):
#     lista.append(pow(2,p))
# for e in lista:
#     print(e)

# lista1=[1,2,3,4]
# lista2=lista1
# lista1.clear()
# print(lista1)
# print(lista2)
#
# lista1=[1,2,3,4]
# lista2=lista1.copy()
# lista1.clear()
# print(lista1)
# print(lista2)

# lista=[1,2,3,4]
# print(lista)
# print(*lista)
#
# def function(*args):
#     pass


# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# lista3=[lista1,lista2]
# print(lista3)
# lista3=[*lista1,*lista2]
# print(lista3)
# print(lista1+lista2)

#
# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# lista1.extend(lista2)
# print(lista1)

# 17. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)
#
# import random
# l1=[]
# l2=[]
# for x in range(10):
#     l1.append(random.randint(1,10))
#     l2.append(random.randint(1, 10))
# print(l1)
# print(l2)
# l3=[*l1,*l2]
# print(l3)
# l1.extend(l2)
# print(l1)

# 18. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
# lista niech zawiera 20 elementów

# lista=[
#     [1,2],
#     [2,4],
#     [3,8],
#     [4,16]
# ]
#
# lista=[]
# for p in range(1,21):
#     lista.append([p,pow(2,p)])
# for e in lista:
#     print(e)


# lista=[]
# for x in range(1,11):
#     lista.append(x)
# for e in lista:
#     print(e)
#
# lista=[e for e in range(1,11)]
# print(lista)
#
# for l in [e for e in range(1,11)]:
#     print(l)
#
# lista=[]
# for x in range(1,11):
#     lista.append(x*10)
# print(lista)
#
# lista=[e*10 for e in range(1,11)]
# print(lista)
#
# lista=[]
# for x in range(1,101):
#     if x%2==0:
#         lista.append(x)
# print(lista)
#
# lista=[e for e in range(1,101) if e%2==0]
# print(lista)
#
# lista=[e for e in range(1,101)]
# druga=[e*100 for e in lista]
# print(lista)
# print(druga)
#
# import random
# lista=[random.randint(1,10) for e in range(100)]
# print(lista)

# 19. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2
#
# lista=[ pow(2,e) for e in range(1,11)  ]
# print(lista)

# 20. Korzystając z list składanych wygeneruj listę 10 elementow której każdy element również będzie listą.
# Pierwszy element tej podlisty to numer potegi, a drugi to wartosc tej potegi dla liczby 2
#
# lista=[]
# for x in range(1,11):
#     lista.append([x,pow(2,x)])
# print(lista)
#
# lista=[ [x,pow(2,x)] for x in range(1,11)]
# print(lista)
#
# linia='1;Andrzej;Klusiewicz;1.76;72\n'
# lista=linia.strip().split(';')
# print(lista)
# print(lista[2])

# 21. Napisz program który z pliku dane.csv wyświetli powiekszone imiona i nazwiska oraz wzrost i masę
#
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])

# 22. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv w taki sposób
# by linie oczyścic z bialych znaków i rozbić na listy. Każdy z elementów listy sam   powinien byc listą.
# Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy   linia po linii.
#
# lista=[]
# for linia in open('dane.csv',encoding='utf-8'):
#     wiersz=linia.strip().split(';')
#     lista.append(wiersz)
# for e in lista:
#     print(e)
#
# #
# # for x in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
# #     print(x)
#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for x in lista:
#     print(x)

# 23. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
# id, imieniu, nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika
#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for x in lista:
#     print(x,type(x[3]))
#
# for linia in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     wzrost=float(linia[3])
#     masa=float(linia[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     print(*linia,bmi)

#
# for linia in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     bmi=round(float(linia[4])/pow(float(linia[3]),2),2)
#     print(*linia,bmi)

#
# for linia in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     print(*linia,round(float(linia[4])/pow(float(linia[3]),2),2))


# for linia in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]: print(*linia,round(float(linia[4])/pow(float(linia[3]),2),2))

# lista=[6,5,4,1,2,5,8,9]
# posortowane=sorted(lista)
# print(lista)
# print(posortowane)

# lista=[6,5,4,1,2,5,8,9]
# lista.insert(6,8)
# lista.sort()
# print(lista)

#
# lista=[6,5,4,1,2,5,8,9]
# lista.sort()
# lista.reverse()
# print(lista)

#
# lista=[6,5,4,1,2,5,8,9]
# lista.sort(reverse=True)
# print(lista)

# lista=[6,5,4,1,2,5,8,9]
# posortowane=sorted(lista,reverse=True)
# print(posortowane)

# 24. Wygeneruj listę 10 elementów o losowej wartości liczbowej, posortuj listę i wyświetl jej zawartość linia po linii
#
# import random
# lista=[random.randint(1,100) for e in range(10)]
# lista.sort()
# for e in lista:
#     print(e)
#
# lista=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# print(lista)
# lista.sort()
# print(lista)
#
# from operator import itemgetter
# lista=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# print(lista)
# lista.sort(key=itemgetter(1))
# print(lista)

#
# from operator import itemgetter
# lista=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# print(lista)
# lista.sort(key=itemgetter(1),reverse=True)
# print(lista)

#
# from operator import itemgetter
# lista=[
#     [2,'A'],
#     [1,'C'],
#     [3,'B']
# ]
# print(lista)
# lista.sort(key=lambda e:e[1])
# print(lista)
#
# class Osoba:
#     imie=None
#     nazwisko=None
#     def __init__(self,imie,nazwisko):
#         self.imie=imie
#         self.nazwisko=nazwisko
#     def __str__(self):
#         return str(self.__dict__)
#
# o1=Osoba('Andrzej','Klusiewicz')
# o2=Osoba('Natalia','Gmurczyk')
# o3=Osoba('Laura','Dawidowska')
# o4=Osoba('Monika','Bożko')
#
# lista=[o1,o2,o3,o4]
# lista.sort(key=lambda o:o.nazwisko)
# for e in lista:
#     print(e)

# 25.  Wczytaj do listy kolejne wiersze z pliku dane.csv.
# Dane posortuj po nazwiskach i wyswietl linia po linii na konsoli.
#
# from operator import itemgetter
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# lista.sort(key=itemgetter(2))
# for e in lista:
#     print(e)

#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# lista.sort(key=lambda e:e[2])
# for e in lista:
#     print(e)

# przerwa do 14:32

# 26. Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi
#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista: l.append( round(float(l[4])/pow(float(l[3]),2),2) )
# lista.sort(key=lambda e:e[5],reverse=True)
# for l in lista:
#     print(l)
#
# lista=[1,2,'koza',3,4]
# lista.sort()

#
# lista=['1','2','koza','3','4']
# lista.sort()
# print(lista)
#
# lista=[1,2,3,4]
# if 2 in lista:
#     print('jest')
# else:
# #     print('nie ma')
#
# linia='siała baba mak'
# if 'bab' in linia:
#     print('jest w stringu')
# else:
#     print('nie ma w stringu')

# lista=['siała','baba','mak']
# if 'bab' in lista:
#     print('jest w liście')
# else:
#     print('nie ma w liście')
#
# lista=['siała','baba','mak']
# for e in lista:
#     if 'bab' in e:
#         print(f'jest fraza w {e}')
#
# import os
# os.mkdir('d:\\nowy')
#
# import os
# for e in os.walk('e:\\'):
#     print(e)

# 27.Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
# Wyszukiwarka ma być nieczuła na wielkość liter
#
# szukane='oracle'
# import os
# for e in os.walk('e:\\'):
#     katalogi=e[1]
#     for k in katalogi:
#         if szukane.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     pliki=e[2]
#     for p in pliki:
#         if szukane.lower() in p.lower():
#             print(os.path.join(e[0],p))
#
# szukane='oracle'
# import os
# for e in os.walk('e:\\'):
#     for k in e[1]:
#         if szukane.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.lower() in p.lower():
#             print(os.path.join(e[0],p))


#
# szukane=input('podaj czego szukasz:\n')
# sciezka=input('podaj katalog startowy:\n')
# import os
# for e in os.walk(sciezka):
#     for k in e[1]:
#         if szukane.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.lower() in p.lower():
#             print(os.path.join(e[0],p))

#
# krotka=(1,2,3,4)
# lista=[1,2,3,4]
# krotka[3]='podmieniono'
# lista[3]='podmieniono'
# print(krotka)
# print(lista)

# krotka=(1,5,2,3,5,4)
# print(krotka[2])
# print(krotka[2:6])
# if 2 in krotka:
#     print('jest')
# else:
#     print('nie ma')
# print(len(krotka))
#
# for k in krotka:
#     print(k)
#
# posortowane=sorted(krotka)
# print(posortowane)

#
# krotka=(1,5,2,3,5,4)
# lista=list(krotka)
# lista.sort()
# krotka=tuple(lista)
# print(krotka)
#
# krotka=(1,5,2,3,5,4)

# def funkcja(wejscie):
#     wejscie='zmienione'
#
# zmienna='xxxx'
# funkcja(zmienna)
# print(zmienna)
#
# def funkcja(krota):
#     lista=list(krota)
#     lista.clear()
#     krota=tuple(lista)
#
# krotka=(1,2,3,4)
# funkcja(krotka)
# print(krotka)


# krotka=(1,2,3,4)
# for e in reversed(krotka):
#     print(e)
#
# krotka=(1,2,3,4)
# print(krotka[-2])

# krotka=(1,2,3,4)
# print(*krotka)

# 28. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10,
# druga 10 losowych liczb zakresu 11-20. Stwórz trzecią krotkę która ma zawierać dane z obu krotek.
# Trzecią krotkę wypisz na konsoli
#
# import random
# krotka1=tuple([random.randint(1,10) for e in range(10)])
# krotka2=tuple([random.randint(11,20) for e in range(10)])
# print(krotka1,type(krotka1))
# print(krotka2,type(krotka2))
# krotka3=(*krotka1,*krotka2)
# print(krotka3)
# krotka3=krotka1+krotka2
# print(krotka3)

# 28. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv
#
# wynik=[tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# for w in wynik:
#     print(w)


# for w in [tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]: print(w)

# z1={1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3}
# print(z1)
#
# lista=[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3]
# zbior=set(lista)
# print(lista)
# print(zbior)
# lista=list(zbior)
# print(lista)
#
# z1={1,2,3,4,5}
# z2={4,5,6,7,8}
# print(z1.intersection(z2))
# print(z1.union(z2))
# print(z1.difference(z2))
# print(z2.difference(z1))

# 29. Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną
#
# z1={1,2,3,4}
# z1.add(5)
# print(z1)

# import random
# z1=set([random.randint(1,40) for e in range(20)])
# #print(z1,type(z1),len(z1))
# z2=set([random.randint(1,40) for e in range(20)])
# print(z1)
# print(z2)
# print("suma=",z1.union(z2))
# print('roznica z1-z2=',z1.difference(z2))
# print('roznica z2-z1=',z2.difference(z1))
# print('czesc wspolna=',z1.intersection(z2))

# 30. Zduplikuj jeden z wierszy w pliku dane.csv.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.

# wynik=list(set([tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]))
# for w in wynik:
#     print(w)
# print(type(wynik))


# plik=open('output.txt',encoding='utf-8',mode='w')
# for x in range(1,11):
#     plik.write(f'element numer {x}\n')
# plik.close()
#
# with open('output.txt',encoding='utf-8',mode='w') as plik:
#     for x in range(1,11):
#         plik.write(f'element numer {x}\n')
# print('koniec')

# 31. Przetwórz plik dane.csv w taki sposób by w efekcie umieścić w pliku output.csv
# dane z pliku dane.csv wzbogacone o obliczone BMI, bez duplikatów i rozwiązując problem  podania
# przecinka w miejsce kropki we wzroście i masie oraz problem z pustymi wierszami.
#
# wynik=[e.strip().replace(',','.').split(';') for e in open('dane.csv') if len(e.strip())>0]
# wynik2=[]
# for w in wynik:
#     bmi=round(float(w[4])/pow(float(w[3]),2),2)
#     w.append(bmi)
#     wynik2.append(tuple(w))
#
# wynik2=list(set(wynik2))
# for w in wynik2:
#     print(w)

#
# linia="1;Andrzej;Klusiewicz"
# lista=linia.split(';')
# print(lista)
# linia_nowa=";".join(lista)
# print(linia_nowa)
#
# lista=[1,'Andrzej','Klusiewicz']
# lista2=[]
# for l in lista:
#     lista2.append(str(l))
# print(";".join(lista2))

# slownik=dict()
# slownik['klucz1']=5
# slownik['klucz2']=[1,2,3,4,5]
# print(slownik['klucz2'])
# for k in slownik.keys():
#     print(k,slownik[k])
#
# for k in slownik:
#     print(k,slownik[k])
#
# for v in slownik.values():
#     print(v)
#
# if 'klucz2' in slownik:
#     print('mamy taki klucz')
# else:
#     print('nie mamy takiego klucza')
#
# print(slownik['nieistniejacy_klucz'])

# 32. Stwórz plik ustawienia.conf i umieść w nim poniższe dane
# encoding=utf-8
# timezone=-2
# color=black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a druga przypisane do nich wartości
# . Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości
# slownik['encoding']
#
# ustawienia=dict()
# for f in [e.strip().split('=') for e in open('ustawienia.conf',encoding='utf-8') if len(e.strip())>0]:
#     ustawienia[f[0]]=f[1]
#
# for k in ustawienia:
#     print(k,ustawienia[k])
#
# print(ustawienia['encoding'])

# 33. Wczytaj do słownika dane z pliku dane.csv tak by kluczem było imię sklejone z
# nazwiskiem rozdzielone spacja, a pozostałe dane znalazły się w wartości
#   jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.
#
# slownik=dict()
# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     slownik[l[1]+" "+l[2]]=(l[0],l[3],l[4])
#
# for k in slownik:
#     print(k,slownik[k])

# 34. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.
#

# nazwa_pliku='tadzio.txt'
# calosc=open(nazwa_pliku,encoding='utf-8').read().lower()
# niechciane=[',','.','!','?','(',')','…',';',':','/','-']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# print(slowa)
# slownik=dict()
#
# import time
# poczatek=time.time()
# nazwa_pliku='tadzio.txt'
# calosc=open(nazwa_pliku,encoding='utf-8').read().lower()
# niechciane=[',','.','!','?','(',')','…',';',':','/','-']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slownik=dict()
# for s in calosc.split():
#     if s in slownik:
#         slownik[s]+=1
#     else:
#         slownik[s]=1
# for k in slownik:
#     print(k,slownik[k])
# koniec=time.time()
# print(f'czas trwania to: {koniec-poczatek}s')


# fuuuu rozwiązanie - tak nie robimy - to przyklad jak mozna to schrzanić

#
# import time
# poczatek=time.time()
# nazwa_pliku='tadzio.txt'
# calosc=open(nazwa_pliku,encoding='utf-8').read().lower()
# niechciane=[',','.','!','?','(',')','…',';',':','/','-']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slownik=dict()
# slowa=calosc.split()
# for s in slowa:
#     print(s,slowa.count(s))
# koniec=time.time()
# print(f'czas trwania to: {koniec-poczatek}s')

#
# import time
# poczatek=time.time()
# nazwa_pliku='tadzio.txt'
# calosc=open(nazwa_pliku,encoding='utf-8').read().lower()
# niechciane=[',','.','!','?','(',')','…',';',':','/','-']
# for n in niechciane: calosc=calosc.replace(n,'')
# slownik=dict()
# for s in calosc.split():
#     if s in slownik:slownik[s]+=1
#     else: slownik[s]=1
# koniec=time.time()
# for w in sorted([ (k,slownik[k]) for k in slownik ],key=lambda e:e[1],reverse=True):
#     print(w)
# print(f'czas trwania to: {koniec-poczatek}s')


# przerwa do 10:25

# 35. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
#
# for x in range(-10,10):
#     print(x,1/x)
#
# try:
#     print(1/0)
#     print('dalej....')
#     print('koniec')
# except:
#     print('jakiś wyjątek....')


# try:
#     print(1/0)
# except:
#     print('jakiś wyjątek....')
# print('dalej....')
# print('koniec')

#
# try:
#     print(1/0)
# except Exception as e:
#     print(f'jakiś wyjątek....{e}')
# print('dalej....')
# print('koniec')


# try:
#     print(1/0)
# except Exception as e:
#     print(f'jakiś wyjątek....{e}')
# print('dalej....')
# print('koniec')

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(f'dzielenie przez zero')
# except IOError:
#     print(f'JAJO error')
# except NotImplementedError:
#     print('nie zaimplementowano')
# except Exception:
#     print('coś jakby else')
# print('dalej....')
# print('koniec')
#
# try:
#     print(1/0)
# # except ZeroDivisionError:
# #     print(f'dzielenie przez zero')
# except IOError:
#     print(f'JAJO error')
# except NotImplementedError:
#     print('nie zaimplementowano')
# except Exception:
#     print('coś jakby else')
# print('dalej....')
# print('koniec')

# #raise ZeroDivisionError
# raise Exception('moja własna treść wyjątku')

# 36. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10 w taki sposob
# by w przypadku wyjatku nie przerywac dzialania petli a po prostu wyswietlic na konsoli informację
# o błędzie i przejsc do dalszego przetwarzania

# for x in range(-10,11):
#     print(x,1/x)

# złe rozwiązanie:
#
# try:
#     for x in range(-10,11):
#         print(x,1/x)
# except ZeroDivisionError:
#     print('dzielenie przez zero....')
#
# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(f'dzielenie przez zero przy x={x}')


# 37. Przetwórz wszystkie wiersze z dane.csv wyswietlajac na konsoli dane z wiersza wzbogacone o bmi.
# Nie podmieniaj przecinków etc w tekscie. W przypadku pojawienia się wyjątku dla
# któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku bledy.csv wzbogacony o informację o rodzaju błędu
# 4;Andrzej;1,89;90;IOERROR
#
# dane=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in dane:
#     try:
#         bmi=round(float(d[4])/pow(float(d[3]),2),2)
#         print(d,bmi)
#     except Exception as e:
#         with open('bledy.csv',encoding='utf-8',mode='a') as plik:
#             plik.write(';'.join(d)+";"+str(e)+"\n")
#

# import time

# def timer(fun):
#     def wewn(*args,**kwargs):
#         s=time.time()
#         fun(*args,**kwargs)
#         k=time.time()
#         print(f'czas trwania to {k-s}s')
#     return wewn
# @timer
# def funkcja():
#     time.sleep(3)
#     print('hello')
#
# funkcja()

# def funkcja():
#     print('hello')
#
# funkcja()


# def funkcja(a,b):
#     print(a+b)
#
# funkcja(10,30)

# def dodaj(a,b):
#     return a+b
#
# print(dodaj(1,3))
# wynik=dodaj(3,4)
# print(wynik)

# def dodaj(a,b):
#     c=a+b
#     return c
#     print('to się nie ma prawa zdarzyć')
#
# print(dodaj(1,3))
# wynik=dodaj(3,4)
# print(wynik)

# def witacz(imie='nie podano',nazwisko='nie podano'):
#     print(f'siema {imie} {nazwisko}!')
#
# def witacz():
#     print('siema')
#
# witacz('Andrzej','Klusiewicz')
# witacz()

# 38. Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.
# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.

# def bmi(wzrost,masa):
#     try:
#         return round(masa/pow(wzrost,2),2)
#     except Exception as e:
#         print(f'wyjątek {e} dla danych wzrost={wzrost}, masa={masa}')
#         return -1
#
# print(bmi(1.76,84))
# print(bmi('wysoki',84))
# print(bmi(0,84))

# 39. Napisz funkcję która zwróci pod postacią listy krotek zawartość pliku
# którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
# podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie pdane ma przyjac utf-8


# def dane(nazwa_pliku,kodowanie="utf-8"):
#     print(f'kodowanie={kodowanie}')
#     return [ tuple(e.strip().split(';')) for e in open(nazwa_pliku,encoding=kodowanie) if len(e.strip())>0]
#
# wynik=dane('dane.csv')
# #wynik=dane('dane.csv','utf-16')
# #print(wynik)
# for w in wynik:
#     print(w)

# przerwa do 11:35

# 40. Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
# przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
# liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
# poprzedniego i przekaz do nowo powstalej funkcji.

# def dane(nazwa_pliku,kodowanie="utf-8"):
#     return [ tuple(e.strip().split(';')) for e in open(nazwa_pliku,encoding=kodowanie) if len(e.strip())>0]
#
# def drukuj(lista):
#     for e in lista:
#         print(e)
#
# wynik=dane('dane.csv')
# drukuj(wynik)
#
# drukuj(dane('dane.csv'))

# 41. Napisz funkcję która przyjmie przez argumenty kwotę lokaty, oprocentowanie w skali roku, ilosc miesięcy.
# Funkcja ma zwrócić zarobek na lokacie o podanych parametrach
#
# def lokata(kwota,oprocentowanie,ilosc_miesiecy):
#     poczatkowo=kwota
#     for m in range(1,ilosc_miesiecy+1):
#         kwota=kwota+(kwota*oprocentowanie/12)
#     return round(kwota-poczatkowo,2)
#
# x=lokata(1000000,0.03,24)
# print(x)

# import time
# def daj_dane():
#     wynik=[]
#     for x in range(1,11):
#         time.sleep(1)
#         wynik.append(f'element numer {x}')
#     return wynik
#
# for dd in daj_dane():
#     print(dd)

#
# import time
# def daj_dane():
#     for x in range(1,11):
#         time.sleep(1)
#         yield f'element numer {x}'
#
# for dd in daj_dane():
#     print(dd)


# import time
# def daj_dane():
#     x=0
#     while True:
#         x+=1
#         time.sleep(1)
#         yield f'element numer {x}'

# for dd in daj_dane():
#     print(dd)
# #
# import time
# def daj_dane():
#     for x in range(1,11):
#         time.sleep(1)
#         yield f'element numer {x}'
#
# d=daj_dane()
# for x in range(20):
#     try:
#         print(next(d))
#     except StopIteration:
#         break

# 42. Stwórz generator który będzie podawał kolejne dni tygodnia (poniedzialek,wtorek etc).
# Przeiteruj po zwracanych przez niego wartosciach i wyswietl je na konsoli

# def dni():
#     yield 'poniedziałek'
#     yield 'wtorek'
#     yield 'środa'
#     yield 'czwartek'
#     yield 'piątek'
#     yield 'sobota'
#     yield 'niedziela'
#
# for d in dni():
#     print(d)

# 43. Stworz generator ktory bedzie przyjmowal przez parametr ilosc elementow a nastepnie zwracal elementy o tresci
# 'element o indeksie x'( gdzie x bedzie numerem podawanego elementu) czekajac 1 sekunde przed zwrotem kazdego elementu.
#
#
# import time
# def generator(max):
#     for x in range(1,max+1):
#         time.sleep(1)
#         yield f'element numer {x}'
#
# for g in generator(10):
#     print(g)
#
#

# 44. Stwórz generator który będzie podawał nieskończenie wiele liczb parzystych.
# Przetestuj go pobierając z niego kolejne wartości i wyświetlając je na konsoli.

# def parzyste(): #złe rozwiązanie
#     x=0
#     while True:
#        x+=1
#        if x%2==0:
#            yield x

# for p in parzyste():
#     print(p)

# def parzyste(): #złe rozwiązanie
#     x=0
#     while True:
#        x+=2
#        yield x
#
# for p in parzyste():
#     print(p)

# 45.     • (do użycia np. w wyszukiwarce - szukaj aż znajdziesz ale nie wczytuj całości od razu)
# Stwórz generator który będzie podawał kolejne linie z pliku tekstowego którego nazwę podamy przez  argument generatora.
# Generator nie powinien wczytywać całego pliku od razu, a w miarę żądania kolejnych elementów powinien wczytywać
# i zwracac kolejne linie z pliku . Użycie funkcji readlines() na obiekcie pliku będzie
# tu więc niewłaściwe, ponieważ wczytuje  ona od razu cały plik, a to mogłoby doprowadzić do przepełnienia pamięci.
# Przykład czytania pliku linia po linii:
#
# plik=open('linie.txt')
# while True:
#     linia=plik.readline()
#     if not linia:
#         break
#     print(linia.strip())
#
# Utworz zmienna w ktorej umiescisz poszukiwana fraze.
# Korzystajac z generatora przeszukuj zwracane przez generator linie w poszukiwaniu poszukiwanej frazy.
# W przypadku znalezienia poszukiwanej frazy w zwracanej przez generator linii chcemy wyswietlic ta linie
# i przerwac przetwarzanie danych z generatora.

# for w in open('dane.csv').readlines():
#     print(w)

# print(len(open('dane.csv').readlines()))

# def czytacz(nazwa_pliku):
#     plik=open(nazwa_pliku,encoding='utf-8')
#     while True:
#         linia=plik.readline()
#         if not linia:
#             break
#         yield linia
#
# szukane='zachód'
# for c in czytacz('tadzio.txt'):
#     if szukane.lower() in c.lower():
#         print(c)
#         break


# suma=0
# for x in range(1,1000):
#     suma+=x

# przerwa obiadowa do 13:00
#
# import time
# def timer(fun):
#     def wewn(*args,**kwargs):
#         s=time.time()
#         fun(*args,**kwargs)
#         k=time.time()
#         print(f'czas trwania to {k-s}s')
#     return wewn
# @timer
# def funkcja():
#     time.sleep(3)
#     print('hello')
#
# funkcja()
#
# def args(*params):
#     print(type(params))
#
# args(1,'koza','nietoperz','toperz')


# def args(*params):
#     print(type(params))
#     for p in params:
#         print(p)
#
# args(1,'koza','nietoperz','toperz')
#
#


# def kwargs(**kwargs):
#     print(type(kwargs))
#     for k in kwargs:
#         print(k,kwargs[k])
#
#
# kwargs(param1='coś',param2=1234)

# def funkcja(moj_parametr,*args,**kwargs):
#     print(f'moj_parametr={moj_parametr}')
#     print(f'args={args}')
#     print(f'kwargs={kwargs}')
#
# funkcja('cos do mojego parametru',1,2,3,4,param1='uuuuu')

# 46. Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args
#
# lista=[1,2,3,4,5]
# print(sum(lista))
# print(max(lista))
# print(min(lista))
# print(sum(lista)/len(lista))

# def suma_args(*args):
#     print(sum(args))
#
# suma_args(1,5,6,3,2)

# 47. Stwórz funkcję która przyjmie nieokreśloną liczbę elementów przez argument, a następnie wypisze
# na konsoli ilość otrzymanych elementów. Poniżej informacji o ilości otrzymanych elementów wyświetl w osobnych
# liniach każdy argument oraz jego typ.
#
# def cw47(*args):
#     print(f'ilość elementów={len(args)}')
#     for a in args:
#         print(a,type(a))
#
# cw47(1,'koza','costam',5.5)

# 48.(kolejnosc argumentów gdy jest args) Stwórz funkcję która przyjmie przez argument mnożnik oraz elementy typu args.
# Funkcja ma dla kazdego elementu typu args wyswietlic na konsoli wynik jego mnożenia przez mnożnik

# def mnozenie(mnoznik,*args):
#     for a in args:
#         print(a*mnoznik)
#
# mnozenie(10,1,2,3,4,5)

# 49. Stworz funkcje "config" ktora bedzie otrzymywala argumenty kwargs bedace ustawieniami.
# Funkcja ta ma zapisac podane argumenty do pliku config.csv w 2 kolumnach z czego pierwsza jest nazwa argumentu
# a druga jego wartoscia. Jesli dane argument juz istnieje w pliku to trzeba bedzie tylko zaktualizowac jego wartosc,
# jesli jeszcze go nie ma to trzeba go bedzie dodac do pliku.

# config(encoding='utf-8',color='black')
#
# encoding=utf-8
# color=black

# def config(**kwargs):
#     dane=[e.strip().split('=') for e in open('config.conf',encoding='utf-8')]
#     slownik=dict()
#     for d in dane:
#         slownik[d[0]]=d[1]
#     for k in kwargs:
#         slownik[k]=kwargs[k]
#     with open('config.conf',encoding='utf-8',mode='w') as plik:
#         for k in slownik:
#             plik.write(f'{k}={slownik[k]}\n')
#
# config(encoding='utf-8',color='red')
#
# slownik=dict()
# slownik['k1']='wartość 1'
# slownik['k2']='wartość 2'
# print(slownik)
# del slownik['k1']
# print(slownik)

#
# def siemator():
#     print('siema!')
#
# def opakowanie(fun):
#     print(fun.__name__)
#
# opakowanie(siemator)

# def obrob(x):
#     return x*100
#
# def opakowanie(fun,y):
#     print(fun(y))
#
# opakowanie(obrob,5)
#
#
# import time
# def funkcja():
#     print('start!')
#     time.sleep(4)
#     print('koniec')
#
# # funkcja()
# # print('dalej coś')
#
# import threading
# t=threading.Thread(target=funkcja)
# t.start()
# print('dalej coś...')

# 50. Stwórz dwie funkcje - jedna ma zwracać powiększony tekst który otrzyma przez argument,
# druga analogicznie ale pomniejszony. Dodaj funkcję która będzie w stanie przyjąć przez argument inną
# funkcję oraz ciąg tekstowy do obróbki który następnie po obrobieniu przez funkcję podaną jako
# argument zostanie wyświetlony na konsoli

# def powieksz(tekst):
#     return tekst.upper()
#
# def pomniejsz(tekst):
#     return tekst.lower()
#
# def cw50(fun,tekst):
#     print(fun(tekst))
#
# cw50(powieksz,'siała BABA mak')
# cw50(pomniejsz,'siała BABA mak')

# 51. Stworz funkcje ktora bedzie drukowala na konsoli dane otrzymane przez pierwszy argument
# obrobione uprzednio przez wyrazenie lambda podane jako drugi argument.

# def cw50(fun,tekst):
#     print(fun.__name__)
#     print(fun(tekst))
#
# cw50(lambda x:x.upper(),'siała BABA mak')
# cw50(lambda x:x.lower(),'siała BABA mak')

# 52. Stwórz funkcję "parse" która będzie otrzymywała przez argumenty wartosc tekstową oraz *args funkcji.
# Funkcja ta ma zastosować każdą z otrzymanych przez *args funkcji na wartości tekstowej którą następnie wypisze na konsoli.
# Dodaj funkcję "powieksz" i "podziel" które mają zwracać otrzymane przez argument dane odpowiednio po powiększeniu
# i podzieleniu tekstu na słowa. Wywołaj funkcję "parse" przekazując do niej ciąg tekstowy składający
# się z więcej niż 1 słowa oraz funkcje "powieksz" i "podziel"

# def powieksz(tekst):
#     return tekst.upper()
#
# def podziel(tekst):
#     return tekst.split()
#
# def parse(tekst,*funcs):
#     for f in funcs:
#         tekst=f(tekst)
#     print(tekst)
#
# parse('siała baba mak',powieksz,podziel)
#
# parse('siała baba mak',lambda x:x.upper(),lambda x:x.split())
#
# def zpomoca(param):
#     '''treść pomocy
#     param musi być tekstem'''
#     pass
#
# help(zpomoca)

#
# def zpomoca(param:str):
#     '''treść pomocy
#     param musi być tekstem'''
#     if type(param) is not str:
#         raise Exception('przyjmuję tekst!')

# help(zpomoca)
#
# fun(String xxx)

# zpomoca(1234)
# zpomoca('dupa')
#
#
# def zewnetrzna():
#     def wewnetrzna():
#         print('siema, jestem funkcją wewnętrzną')
#     return wewnetrzna
#
# f=zewnetrzna()
# f()

# 53. Stwórz funcję która będzie posiadała dwie funkcje wewnętrzne.
# Jedna z tych funkcji ma powiekszac i zwracac otrzymany ciag znakow, druga pomniejszac i zwracac otrzymany ciąg znaków.
# Funkcja zewnętrzna ma zwracać funkcję powiększającą gdy zostanie jej przez argument przekazana wartosc 1 i
# funkcję pomniejszającą gdy otrzyma wartość 2. Odbierz obiekt funkcji wewnętrznej poprzez wywołanie funkcji zewnętrznej
# i zastosuj otrzymaną funkcję na ciągu tekstowym.

#
# def oddaj_funkcje(x):
#     def powieksz(tekst):
#         return tekst.upper()
#     def pomniejsz(tekst):
#         return tekst.lower()
#
#     if x==1:
#         return powieksz
#     elif x==2:
#         return pomniejsz
#     else:
#         raise NotImplementedError()
#
# funkcja=oddaj_funkcje(1)
# print(funkcja('siała BABA mak'))
# funkcja=oddaj_funkcje(2)
# print(funkcja('siała BABA mak'))

# funkcja=oddaj_funkcje(3)
# print(funkcja('siała BABA mak'))

# przerwa do 14:24
#
# class Whatever{
#     public static void main(String args[]){
#         System.out.println('dupa');
#     }
# }
#
# print('dupa')
#
# def dekorator(fun):
#     def wewnetrzna():
#         print('dekorator!')
#         fun()
#     return wewnetrzna
#
# def funkcja():
#     print('hello...')
#
# fun=dekorator(funkcja)
# fun()

# @dekorator
# def funkcja():
#     print('hello...')

# funkcja()

#
# def opakowanie(fun):
#     def wewnetrzna():
#         print('dekorator!')
#         fun()
#     return wewnetrzna
#
# @opakowanie
# def funkcja():
#     print('hello...')
#
# funkcja()

# fun=dekorator(funkcja)
# fun()


# def opakowanie(fun):
#     def wewnetrzna(*args,**kwargs):
#         print('dekorator!')
#         fun(*args,**kwargs)
#     return wewnetrzna
#
# @opakowanie
# def funkcja(imie):
#     print(f'hello {imie}')
#
# @opakowanie
# def funkcja2(imie,nazwisko):
#     print(f'hello {imie} {nazwisko}')
#
# @opakowanie
# def funkcja3():
#     print('hello!')
#
# funkcja('Andrzej')
# funkcja2('Andrzej','Klusiewicz')
# funkcja3()

# def opakowanie(fun):
#     def wewnetrzna(*args,**kwargs):
#         print('dekorator!')
#         return fun(*args,**kwargs)
#     return wewnetrzna
#
# @opakowanie
# def oddaj_koze():
#     return "koza"
# print(oddaj_koze())
#
# fun=opakowanie(oddaj_koze)
# print(fun())
#
# def opakowanie(fun):
#     def wewnetrzna(*args,**kwargs):
#         print('sprawdzenie czasu przed')
#         z= fun(*args,**kwargs)
#         print('sprawdzenie czasu po')
#         print('wyświetlecnie czasu trwania naszej dekorowanej funkcji')
#         return z
#     return wewnetrzna
#
# @opakowanie
# def oddaj_koze():
#     return "koza"
# print(oddaj_koze())

# 54. Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
# Dodaj dekorator który zliczy czas wykonywania tej funkcji. Pobranie aktualnego czasu to: "time.time()",
# wstrzymanie na 3 sekundy: "time.sleep(3)"
#
# import time
# poczatek=time.time()
# time.sleep(2)
# koniec=time.time()
# print(f'czas: {koniec-poczatek}s')
# import time
# def timer(fun):
#     def wewnetrzna(*args,**kwargs):
#         poczatek=time.time()
#         wynik=fun(*args,**kwargs)
#         koniec=time.time()
#         print(f'czas trwania funkcji {fun.__name__} wynosi {koniec-poczatek}s')
#         return wynik
#
#     return wewnetrzna
#
# @timer
# def spioch():
#     time.sleep(3)
#     return 66
#
# x=spioch()
# print(f'odebrane={x}')

# 55. Stwórz dekodator który będzie zawsze zaokrąglał do 2 miejsc po przecinku wynik zwracany przez dekordowaną funkcję.
#
# def dodatkowy(fun):
#     def wewnetrzna(*args,**kwargs):
#         print('dodatkowy dekorator')
#         return fun(*args,**kwargs)
#     return wewnetrzna
# def zaokraglacz(fun):
#     def wewnetrzna(*args,**kwargs):
#         return round(fun(*args,**kwargs),2)
#     return wewnetrzna
#
# @zaokraglacz
# @dodatkowy
# def daj_liczbe():
#     print('koza!')
#     return 10/3
#
# print(daj_liczbe())
#
# def powtorz(x):
#     def dekorator(fun):
#         def wewnetrzna(*args,**kwargs):
#             for i in range(1,x+1):
#                 fun(*args,**kwargs)
#         return wewnetrzna
#     return dekorator
# @powtorz(10)
# def funkcja():
#     print('hello')
#
# funkcja()
#
# @app.route('/show_participant_details')
# def widok_szczegolow_uczestnika():
#     pass

# 56.    • Stwórz dekorator który będzie rejestrował do pliku loga wszystkie wywołania dekorowanej funkcji
# z informacją o nazwie dekorowanej funkcji, dacie i czasie jej wywołania oraz argumentach przekazanych
# do dekorowanej funkcji. Log ma być w formacie CSV. Same argumenty powinny być rejestrowane w jednej kolumnie razem.
# Pobranie nazwy funkcji: fun.__name__,
# Pobranie aktualnego czasu i daty:
# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%d/%m/%Y %H:%M:%S"))
#
# #fun.__name__
# import time
#
# def logger(fun):
#     def wewnetrzna(*args,**kwargs):
#         from datetime import datetime
#         now = datetime.now()
#         print(fun.__name__,now.strftime("%d/%m/%Y %H:%M:%S"),args,kwargs)
#         return fun(*args,**kwargs)
#     return wewnetrzna
#
# @logger
# def funkcja(x):
#     time.sleep(x)
#
# funkcja(1)

#
# #fun.__name__
# import time
#
# def logger(fun):
#     def wewnetrzna(*args,**kwargs):
#         from datetime import datetime
#         now = datetime.now()
#         with open('logger.log',encoding='utf-8',mode='a') as plik:
#             plik.write(f"{fun.__name__};{now.strftime('%d/%m/%Y %H:%M:%S')};{args}{kwargs}\n")
#         return fun(*args,**kwargs)
#     return wewnetrzna
#
# @logger
# def funkcja(x):
#     time.sleep(x)
#
# funkcja(1)
# funkcja(2)
# funkcja(3)


# fun.__name__
# import time
#
# def logger(fun):
#     def wewnetrzna(*args,**kwargs):
#         start=time.time()
#         wynik=fun(*args, **kwargs)
#         koniec=time.time()
#         from datetime import datetime
#         now = datetime.now()
#         with open('logger.log',encoding='utf-8',mode='a') as plik:
#             plik.write(f"{fun.__name__};{now.strftime('%d/%m/%Y %H:%M:%S')};{args}{kwargs};{wynik};{koniec-start}s\n")
#         return wynik
#     return wewnetrzna
#
# @logger
# def funkcja(x):
#     time.sleep(x)
#     return f"spałem {x} sekund"
#
# funkcja(1)
# funkcja(2)
# funkcja(3)
#
# #select avg(czas_trwania )from logi where funkcja='jakastam'
# select function, avg(timing) from logs group by function order by 2 desc;
# import functools
# import time
# @functools.lru_cache(maxsize=10)
# def dzialanie(x):
#     time.sleep(1)
#     return x*10
#
# p=time.time()
# for _ in range(10):
#     for i in range(1,4):
#         dzialanie(i)
# k=time.time()
# print(f'{k-p}s')

# import modul
# modul.funkcja()
#
# import modul as m
# m.funkcja()
#
# from modul import funkcja
# funkcja()

# import dao.client_dao as cdao
# import dao.invoice_dao as idao
# print(cdao.get_all())
# print(idao.get_all())
#
# from dao.client_dao import *
# from dao.invoice_dao import *
# print(get_all())

# import dao.client_dao
# print(dao.client_dao.get_all())
# import modul

# import this

# import pakiecik.modul_pakietowy

# 57. Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było  podawać nazwy pakietu ani modułu.
#
# from pakiet.modul import bmi
# print(bmi(1.76,67))

# Postman
#
# import requests
# response=requests.get('https://jsystems.pl/static/blog/python/dane.json')
# if response.status_code==200:
#     data=response.json()
#     print(data['nazwisko'])
#     address=data['adres']
#     print(address['miasto'])
#     print(data['adres']['miasto'])
#     languages=data['jezyki']
#     for l in languages:
#         print(l)
#     for e in data['jezyki']:
#         print(e)
# else:
#     print(f'Nie pobrano danych. Odpowiedź serwera: {response.status_code}')
#
# import requests
# data=dict()
# data['adres']='Żelazna 59 Warszawa'
# data['nazwa_firmy']='JSystems'
# response=requests.post('https://jsystems.pl/static/blog/python/dane.json',data=data, headers={"Content-Type":"application/json"})
# print(response.status_code)

# 58. z usługi sieciowej http://jsystems.pl/Universe/samaTabelka.do pobierz informację o szkoleniach.
# na konsoli wyswietl tytuly, miasta i daty wszystkich szkolen które w tytule mają malymi badz duzymi
# literami "Python","Java", "UML" i status terminu gwarantowanego (pole terminyGwarantowany=1)
#
# import requests
# response=requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code==200:
#     data=response.json()
#     for t in data:
#         print(t)
# else:
#     print(f'operacja nieudana. Status code={response.status_code}')

#
# import requests
#
# response = requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code == 200:
#     data = response.json()
#     for t in data:
#         if ('java' in t['tytul_szkolenia'].lower() \
#             or 'python' in t['tytul_szkolenia'].lower() \
#             or 'uml' in t['tytul_szkolenia'].lower()) and t['terminyGwarantowany']==1:
#             print(t['tytul_szkolenia'],t['miasto'],t['termin'])
# else:
#     print(f'operacja nieudana. Status code={response.status_code}')



# import requests
# response = requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code == 200:
#     data = response.json()
#     for t in [t for t in response.json() if ('java' in t['tytul_szkolenia'].lower() or 'python' in t['tytul_szkolenia'].lower() or 'uml' in t['tytul_szkolenia'].lower()) and t['terminyGwarantowany']==1]:
#         #print(t['tytul_szkolenia'],t['miasto'],t['termin'])
#         print(f"{t['tytul_szkolenia']} {t['miasto']} {t['termin']}")
# else:
#     print(f'operacja nieudana. Status code={response.status_code}')

#BeautifulSoup https://blog.jsystems.pl/show_post/Parsowanie_stron_internetowych_z_u%C5%BCyciem_Beautiful_Soup/
#Wyrażenia regularne https://blog.jsystems.pl/show_post/Wyra%C5%BCenia_regularne/

#przerwa do 9:58

#pgadmin4

#DBeaver
#
# import psycopg2
# connection=psycopg2.connect(host='localhost',database='aplikacja',port=5432, user='aplikacja', password='oracle')
# connection.close()

#
# import psycopg2
# with psycopg2.connect(host='localhost',database='aplikacja',port=5432, user='aplikacja', password='oracle') as connection:
#     pass


#SQLAlchemy
#DjangoORM

#Product.objects.all()
#product.save()
#
# import psycopg2
# with psycopg2.connect(host='localhost',database='aplikacja',port=5432, user='aplikacja', password='oracle') as connection:
#     cursor=connection.cursor()
#     cursor.execute('select * from produkty')
#     for w in cursor:
#         print(w[1])
#

#59. Stwórz tabelkę pracownicy. Niech posiada ona kolumny id_pracownika,imię,nazwisko,telefon. Wstaw
# 3 pracowników do tabeli i upewnij się że się tam znajdują. Napisz funkcję która przyjmie przez parametr
# nazwę pliku do którego zapisze wszystkie wiersze z tabelki pracownicy w fomacie csv.
#
# import psycopg2
# def export(filename):
#     with psycopg2.connect(host='localhost',database='aplikacja',port=5432, user='aplikacja', password='oracle') as connection:
#         cursor=connection.cursor()
#         cursor.execute('select * from pracownicy')
#         with open(filename,encoding='utf-8',mode='w') as file:
#             for w in cursor:
#                 file.write(f'{w[0]};{w[1]};{w[2]};{w[3]}\n')
#
# export('pracownicy.csv')
#
# import psycopg2
# with psycopg2.connect(host='localhost',database='aplikacja',port=5432, user='aplikacja', password='oracle') as connection:
#     cursor=connection.cursor()
#     imie='Tomasz'
#     nazwisko='Janicki'
#     telefon=333
#     cursor.execute(f"insert into pracownicy(imie,nazwisko, telefon) values ('{imie}','{nazwisko}','{telefon}')")
#     connection.commit()

#60. Załaduj do tabelki zawodnicy wszystkie dane z pliku dane.csv
#
# import psycopg2
# with psycopg2.connect(host='localhost',database='aplikacja',port=5432, user='aplikacja', password='oracle') as connection:
#     cursor=connection.cursor()
#     for e in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]:
#         sql=f"insert into zawodnicy values ({e[0]},'{e[1]}','{e[2]}',{e[3]},{e[4]})"
#         print(sql)
#         cursor.execute(sql)
#     connection.commit()

#przerwa do 11:34
#
# class Person:
#     first_name=None
#     last_name=None
#
# p1=Person()
# p1.first_name="Andrzej"
# p1.last_name='Klusiewicz'
#
# p2=Person()
# p2.first_name='Jan'
# p2.last_name='Nowak'
#
# print(p1.first_name,p1.last_name)
# print(p2.first_name,p2.last_name)

#
# class Person:
#     first_name=None
#     last_name=None
#     def show(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')
#
# p1=Person()
# p1.first_name="Andrzej"
# p1.last_name='Klusiewicz'
#
# p2=Person()
# p2.first_name='Jan'
# p2.last_name='Nowak'
# #
# p1.show()
# p2.show()

#61. Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
# Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
# Stwórz dwa obiekty tej klasy (uzupełnij je danymi)
# i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.
#
# class Samochod:
#     marka=None
#     model=None
#     rejestracja=None
#     def wyswietl(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
#
#
# s1=Samochod()
# s1.marka='Polonez'
# s1.model='Caro'
# s1.rejestracja='W0 ZABYTEK'
#
# s2=Samochod()
# s2.marka='Czarny'
# s2.model='Ciągnik'
# s2.rejestracja='2400'
#
# s1.wyswietl()
# s2.wyswietl()
#
# class ABC:
#     def wypisz_cos(self,cos):
#         print(cos)
#
# abc=ABC()
# abc.wypisz_cos('terefere kuku')


#62. Zadbaj o to by klasa Samochod posiadała metodę pozwalającą ustawić wartości wszystkich pól.
# Jej przykładowe wywołanie: s1.ustaw_wartosci(‘Renault’,’Kadjar’,’WE968RP’)
# class Samochod:
#     marka=None
#     model=None
#     rejestracja=None
#
#     def ustaw(self,marka,model,rejestracja):
#         self.marka=marka
#         self.model=model
#         self.rejestracja=rejestracja
#     def wyswietl(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
#
#
# s1=Samochod()
# s1.ustaw('Audi','A4','ABC 1234')
# s2=Samochod()
# s2.ustaw('BMW','e46','WWL 1234')
#
# s1.wyswietl()
# s2.wyswietl()
#
# class Person:
#     first_name=None
#     last_name=None
#     def set_all(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def show(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')
#
# p1=Person()
# #p1.set_all('Andrzej','Klusiewicz')
# p1.show()

#
# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self):
#         print('tworzenie obiektu')
#     def set_all(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def show(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')
#
# p1=Person()
#p1.set_all('Andrzej','Klusiewicz')
#p1.show()

#
# class Person:
#     def __init__(self,first_name,last_name):
#         print('tworzenie obiektu')
#         self.first_name = first_name
#         self.last_name = last_name
#     def show(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')
#
# p1=Person('Andrzej','Klusiewicz')
# p1.description='Twój stary'
# p1.show()
# print(p1.description)


#63. Dodaj do klasy Samochód konstruktor wymuszający ustawienie wartości wszystkich pól przy tworzeniu obiektu.
#    Stworz obiekt klasy samochod i wywolaj na nim metode wyswietl
#
# class Samochod:
#     def __init__(self,marka,model,rejestracja):
#         self.marka=marka
#         self.model=model
#         self.rejestracja=rejestracja
#     def wyswietl(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
#
# s=Samochod('Renault','Karjar','WY 722CP')
# s.wyswietl()

#
# class Samochod:
#     def __init__(self,marka='nie podano',model='nie podano',rejestracja='nie podano'):
#         self.marka=marka
#         self.model=model
#         self.rejestracja=rejestracja
#     def wyswietl(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
#
# s=Samochod('Renault','Karjar','WY 722CP')
# s.wyswietl()
#
# s=Samochod()
# s.wyswietl()
#
# s=Samochod('Renault')
# s.wyswietl()
#
# s=Samochod(model="Kadjar")
# s.wyswietl()

#64.Stwórz klasę Zawodnik posiadającą pola wzrost i masa. Pola te mają być uzupełniane przy tworzeniu obiektu.
# Dodaj do klasy metodę get_bmi która zwróci obliczone na podstawie pól BMI.
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.