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