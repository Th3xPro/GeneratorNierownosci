import random
from sympy import *
import re
import os

# Losowanie czy cyfra jest dodatnia czy ujemna


def PlusMinus(x):
    if(x == 0):
        return ('-' if random.randrange(2) == 0 else '')
    elif(x == 1):
        return ('-' if random.randrange(2) == 0 else '+')

# Losowanie cyfry


def LosowaCyfra(x):
    return random.randrange(1, x+1)

# Metoda losowania znaku wiekszosci/miejszosci


def LosowyZnakWM():
    znaki = ['<', '>', '<=', '>=']
    return random.choice(znaki)

# Metoda tworzenia zadania


def LosowanieZadania():
    los = random.randrange(1, 7)
    x = Symbol('x')
    if(los == 1):
        skladowe = [PlusMinus(0), LosowaCyfra(30), PlusMinus(
            0), LosowaCyfra(30), PlusMinus(1), LosowaCyfra(30), LosowyZnakWM()]
        zadanie = "{}{}x({}{}x{}{}){}0".format(*skladowe)
        zadanieDoRoz = "{}{}*x*Abs({}{}*x{}{}){}0".format(*skladowe)
        rozwiazanie = solve_univariate_inequality(parse_expr(zadanieDoRoz), x)
        return zadanie, rozwiazanie
    elif(los == 2):
        skladowe = [PlusMinus(0), LosowaCyfra(30), PlusMinus(1), LosowaCyfra(
            30), PlusMinus(0), LosowaCyfra(30), PlusMinus(1), LosowaCyfra(30), LosowyZnakWM()]
        zadanie = "({}{}x{}{})({}{}x{}{}){}0".format(*skladowe)
        zadanieDoRoz = "Abs({}{}*x{}{})*Abs({}{}*x{}{}){}0".format(*skladowe)
        rozwiazanie = solve_univariate_inequality(parse_expr(zadanieDoRoz), x)
        return zadanie, rozwiazanie
    elif(los == 3):
        skladowe = [PlusMinus(0), LosowaCyfra(30), PlusMinus(
            1), LosowaCyfra(30), PlusMinus(1), LosowaCyfra(30), LosowyZnakWM()]
        zadanie = "{}{}x**2{}{}x{}{}{}0".format(*skladowe)
        zadanieDoRoz = "{}{}*x**2{}{}*x{}{}{}0".format(*skladowe)
        rozwiazanie = solve_univariate_inequality(parse_expr(zadanieDoRoz), x)
        return zadanie, rozwiazanie
    elif(los == 4):
        skladowe = [PlusMinus(0), LosowaCyfra(30), PlusMinus(
            1), LosowaCyfra(30), LosowyZnakWM()]
        zadanie = "{}{}x{}{}x**2{}0".format(*skladowe)
        zadanieDoRoz = "{}{}*x{}{}*x**2{}0".format(*skladowe)
        rozwiazanie = solve_univariate_inequality(parse_expr(zadanieDoRoz), x)
        return zadanie, rozwiazanie
    elif(los == 5):
        skladowe = [PlusMinus(0), LosowaCyfra(30), LosowyZnakWM(), PlusMinus(
            0), LosowaCyfra(30), PlusMinus(1), LosowaCyfra(30)]
        zadanie = "{}{}x{}{}{}x**2{}{}".format(*skladowe)
        zadanieDoRoz = "{}{}*x{}{}{}*x**2{}{}".format(*skladowe)
        rozwiazanie = solve_univariate_inequality(parse_expr(zadanieDoRoz), x)
        return zadanie, rozwiazanie
    elif(los == 6):
        skladowe = [PlusMinus(0), LosowaCyfra(30), PlusMinus(
            1), LosowaCyfra(30), LosowyZnakWM(), PlusMinus(0), LosowaCyfra(30), PlusMinus(1), LosowaCyfra(30)]
        zadanie = "{}{}x**2{}{}x{}{}{}x{}{}".format(*skladowe)
        zadanieDoRoz = "{}{}*x**2{}{}*x{}{}{}*x{}{}".format(*skladowe)
        rozwiazanie = solve_univariate_inequality(parse_expr(zadanieDoRoz), x)
        return zadanie, rozwiazanie


# Funkcja czyszczenia konsoli
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# Funkcja Sprawdzenia odpowiedzi


def SprawdzOdpowiedz(poprawna_odpowiedz, odpowiedz):
    if(poprawna_odpowiedz == False):
        if(odpowiedz in {'0', 'brak rozwi??za??', 'False', 'B????dna nierowno????', 'fa??sz', 'zero', 'b????d'}):
            return print("Brawo! Twoja odpowied?? jest poprawna!")
        else:
            return print("Niestety nie by??a to prawdziwa odpowied??. \n Odpowied?? to - Brak rozwi??za??")
    else:
        LstOdpPop = KreatorListyOdpowiedzi(poprawna_odpowiedz)
        LstOdpUzy = KreatorListyOdpowiedzi(odpowiedz)
        if(len(LstOdpPop) == len(LstOdpUzy) and len(LstOdpPop) == sum([1 for i, j in zip(LstOdpPop, LstOdpUzy) if i == j])):
            return print("Brawo! Twoja odpowied?? jest poprawna!")
        else:
            return print("Niestety nie by??a to prawdziwa odpowied??. \n Odpowied?? to - {}".format(poprawna_odpowiedz))

# Funkcja tworzenie listy odpowiedzi z systemu i uzytkownika


def KreatorListyOdpowiedzi(odpowiedz):
    output = str(odpowiedz).replace(
        "((", "(").replace("))", ")").replace(" ", "")
    output = re.split('&|\|', output)
    listaZnakow = []
    for x in str(odpowiedz):
        if(x == '&' or x == '|'):
            listaZnakow.append(x)
    i = 1
    for x in listaZnakow:
        if i < len(output):
            output.insert(i, x)
        i += (2)
    return output


# G????wne Zadanie
clearConsole()
zadanie = LosowanieZadania()
print('Twoja zadanie to {}'.format(zadanie[0]))
print("Napisz 'H' ??eby wy??wietli?? znaki pomocnicze")
print("Podaj odpowied?? na zadanie -")
odpowiedz = input()
while len(odpowiedz) == 0 or (odpowiedz.lower() == 'h'):
    if(len(odpowiedz) == 0):
        clearConsole()
        print("Przynajmniej napisz co??")
        print("Zadanie - "+zadanie[0])
        print("Podaj odpowied?? na zadanie -")
        odpowiedz = input()
    elif(odpowiedz.lower() == 'h'):
        clearConsole()
        print('Znaki pomocnicze')
        print('oo <- niesko??czono????')
        print('|  <- lub')
        print('&  <- oraz')
        print('sqrt(x) <- pierwiastek, gdzie x to liczba')
        print('Eq(x,y) <- r??wnanie, gdzie x i y to cyfry')
        print('Fa??sz   <- je??li rozwi??zanie nie ma odpowiedzi lub jest b????dne')
        print()
        print("Zadanie - "+zadanie[0])
        print("Podaj odpowied?? na zadanie -")
        odpowiedz = input()
SprawdzOdpowiedz(zadanie[1], odpowiedz)
