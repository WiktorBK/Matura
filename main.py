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
    return liczby_pierwsze

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

    return result

########################################################################

#Sprawdza czy podana wartosc jest palindromem
def czy_palindrom(s):
    s = str(s)
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]

########################################################################

#Sprawdza czy podane dwie wartosci sa anagramami

def czy_anagram(s1, s2):
    s1, s2 = str(s1), str(s2)
    s1 , s2 = s1.replace(" ", "").lower(), s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

########################################################################

#rozklada liczbe na czynniki pierwsze
def rozloz(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k +=1
    return czynniki

