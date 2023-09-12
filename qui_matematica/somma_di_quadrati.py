import math


def main():
    numero = 99401
    radice = int(math.sqrt(numero))
    print("la radice è", radice)

    for a in range(radice):
        quadrato_a = a*a
        differenza = numero - quadrato_a
        b = int(math.sqrt(differenza))
        if b*b - differenza == 0:
            print(a, " ", b)


main()
