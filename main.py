#test
#Andrzej Klusiewicz
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


#1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
#wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
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

#print('xyz'*10)


#
# liczba=float(input('podaj liczbę:\n'))
# print(liczba,type(liczba))
# print(liczba/2)

#
#
# liczba=int(input('podaj liczbę:\n'))
# print(liczba,type(liczba))
# print(liczba/2)

#2. • BMI= masa/(wzrost*wzrost) .
# Napisz program który odbierze od użytkownika jego masę w kilogramach i wzrost w metrach,
# wyliczy i wypisze BMI.

#print(pow(1.76,2))
#
# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# bmi=round(masa/pow(wzrost,2),2)
# print(f"bmi={bmi}")

#przerwa do 10:31


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

#3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość z informacją "wartość dodatnia",
# jeśli zero to wyświetlamy z informacją "równe zero", jeśli ujemna to wyświetlamy "wartość ujemna".

# x=int(input('podaj liczbę:\n'))
# if x>0:
#     print(f'x={x} jest dodatni')
# elif x==0:
#     print(f'x={x} jest równy zero')
# else:
#     print(f'x={x} jest ujemny')


#4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#wyświetlił nam również odpowiedni opis wg skali z Wikipedii.
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

#help(range)
#
# for x in range(1,11):
#     print(x)
# print('koniec')

#5. Wyświetl 20 kolejnych potęg liczby 2
#
# for p in range(1,21):
#     print(f"2^{p}={pow(2,p)}")


#for p in range(1,21): print(f"2^{p}={pow(2,p)}")
#
# for p in range(1,21):
#     print(f"2^{p}={pow(2,p)}")
#     if 1==1:
#         pass


#6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#parzysta czy nieparzysta
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

#7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
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

#8. Napisz korzystajac z petli while program który wyświetli
#   10 kolejnych potęg liczby 2.
#
# p=1
# while p<=10:
#     print(p,pow(2,p))
#     p += 1
#     #p=p+1
#

#9. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość  potęgi
# nie przekroczy wartości podanej przez użytkownika
#
# max=int(input('podaj maksymalną wartość:\n'))
# potega=0
# np=0
# while potega<=max:
#     np+=1
#     potega=pow(2,np)
#     print(potega)

#10. Napisz program który będzie dodawał kolejne losowe wartości z zakresu
#od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od wartosci podanej przez uzytkownika

# import random
# print(random.randint(1,100))

# import random
# max=int(input('podaj max zakres:\n'))
# suma=0
# while suma<=max:
#     suma+=random.randint(1,10)
#     print(f'suma={suma}')


#przerwa do 11:41
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

#11. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z niego znaki ,.!?
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

#12. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik

# nazwa_pliku=input('podaj nazwę pliku:\n')
# for linia in open(nazwa_pliku,encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(linia.strip())
#
# calosc=open('tadzio.txt',encoding='utf-8').read()
# print(calosc)
# print(calosc.count('a'))

#13. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego
# podanego przez użytkownika w pliku którego nazwę również poda użytkownik.

# szukane=input('podaj szukane:\n')
# nazwa_pliku=input('podaj nazwę pliku:\n')
# print(  open(nazwa_pliku,encoding='utf-8').read().lower().count( szukane.lower()  )  )


# print(  open(input('podaj nazwę pliku:\n'),encoding='utf-8').read().lower().count( input('podaj szukane:\n').lower()  )  )
#print('siema')
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

#14. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
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

#15. Napisz program który będzie od uzytkownika przyjmowal nazwę pliku z kodem pythona.
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

#przerwa do 13:00

#listy, krotki, słowniki, zestawy
#
# lista=[]
# lista=list()
# lista=[1,2,3,4]
# print(lista,type(lista))
# lista.append(5)
# lista.append(6)
# for element in lista:
#     print(element)

#16. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
#Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
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

#17. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
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

#18. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
#lista niech zawiera 20 elementów

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

#19. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2
#
# lista=[ pow(2,e) for e in range(1,11)  ]
# print(lista)

#20. Korzystając z list składanych wygeneruj listę 10 elementow której każdy element również będzie listą.
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

#21. Napisz program który z pliku dane.csv wyświetli powiekszone imiona i nazwiska oraz wzrost i masę
#
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])

#22. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv w taki sposób
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

#23. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
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


#for linia in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]: print(*linia,round(float(linia[4])/pow(float(linia[3]),2),2))

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

#24. Wygeneruj listę 10 elementów o losowej wartości liczbowej, posortuj listę i wyświetl jej zawartość linia po linii
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

#25.  Wczytaj do listy kolejne wiersze z pliku dane.csv.
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

#przerwa do 14:32

#26. Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi
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

#27.Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
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


#krotka=(1,2,3,4)
# for e in reversed(krotka):
#     print(e)
#
# krotka=(1,2,3,4)
# print(krotka[-2])

# krotka=(1,2,3,4)
# print(*krotka)

#28. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10,
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

#28. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv
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

#29. Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
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

#30. Zduplikuj jeden z wierszy w pliku dane.csv.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.