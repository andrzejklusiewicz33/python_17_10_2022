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