'''
przydatne funkcje na mature
'''


#znajduje liczby pierwsze w zakresie 2 do n
def sito_erastotenesa(n):
    liczby_pierwsze = []
    for liczba in range(2, n):
        for liczba_pierwsza in liczby_pierwsze:
            if liczba % liczba_pierwsza == 0:
                break
        else:
            liczby_pierwsze.append(liczba)
    return f"\nliczby pierwsze w zakresie 2 - {n}: \n{liczby_pierwsze}\n"
print(sito_erastotenesa(100))

#####################################################################

#Znajduje największy wspólny dzielnik (Wersja rekurencyjna)
def NWD(a, b):
    if b > 0:
        return NWD(b, a%b)
    return a


#Znajduje największy wspólny dzielnik (Wersja Iteracyjna)
def NWD_I(a, b):
    while b:
        a,b = b, a%b
    return a

#######################################################################

#Znajduje najmniejsza wspólną wielokrotność np: dla 3 i 4 jest to 12
# Z wykorzystaniem NWD
def NWW(a, b):
    return a*b//NWD(a, b)

#drugi sposób
def NWW_2(a, b):
  if (a < b):
    return NWW(b, a)
  k = a
  while (k % b != 0):
    k += a
  return k

########################################################################

def silnia(n):
    if n <= 1:
        return 1
    else:
        return n * silnia(n-1)

########################################################################

#Wypisuje n liczb ciągu fibonacciego
def ciag_fibonacciego(n):
    result = [1, 1]
    for i in range(n - 2):
        result.append(result[i] + result[(i + 1)])

    return f"Pierwsze {n} liczb ciagu fibonacciego to: \n{result}\n"
print(ciag_fibonacciego(15))
########################################################################

#Sprawdza czy podana wartosc jest palindromem
def czy_palindrom(s):
    s = str(s)
    s = s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        return f"{s} jest palindromem\n"
    else:
        return f"{s} nie jest palindromem\n"
print(czy_palindrom("kajak"))
########################################################################

#Sprawdza czy podane dwie wartosci sa anagramami

def czy_anagram(s1, s2):
    s1, s2 = str(s1), str(s2)
    s1 , s2 = s1.replace(" ", "").lower(), s2.replace(" ", "").lower()
    if sorted(s1) == sorted(s2):
        return f"{s1} i {s2} są anagramami\n"
    else:
        return f"{s1} i {s2} nie są anagramami\n"
print(czy_anagram("niedziela", "dzielenia"))
########################################################################

#rozklada liczbe na czynniki pierwsze
def rozloz(n):
    i = n
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k +=1
    return f"czynniki pierwsze liczby {i} to: \n{czynniki}\n"
print(rozloz(15))
###############################################################################

#szyfruje napis szyfrem cezara

def szyfr_cezara(s, n):
    szyfr = ""
    for i in range(len(s)):
        liczba = ord(s[i])  # zapisuje dana literke z napisu w postaci liczby
        szyfr += chr(liczba + n)
    return f"Szyfr cezara słowa {s} po przesunieciu o {n} to: \n{szyfr}\n"
print(szyfr_cezara("ABDSDFHGASDGSD", 6))
###############################################################################

#Zwraca dzielniki danej liczby
def dzielniki(n):
    dzielniki = []
    for a in range(1, (int(n/2)) + 1):
        if n % a == 0:
            dzielniki.append(a)
    return dzielniki
print("Dzielnikami liczby 1024 oprócz jej samej są:")
print(dzielniki(1024))
################################################################################

#Sprawdza czy podana liczba jest doskonała z wykorzystaniem funkcji dzielniki()
def czy_doskonala(n):
    suma = 0
    for i in dzielniki(n):
        suma += i
    if suma == n:
        return f"\nLiczba {n} jest liczba doskonala"
    else:
        return f"\nLiczba {n} nie jest liczba doskonala"
print(czy_doskonala(28))