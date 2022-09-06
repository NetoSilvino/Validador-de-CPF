'''
Gerador de CPF.
1 * 10 = 10     #   1 * 11 = 11
6 * 9 = 54      #   6 * 10 = 60
8 * 8 = 64      #   8 * 9 = 72
9 * 7 = 63      #   9 * 8 = 72
9 * 6 = 54      #   9 * 7 = 63
5 * 5 = 25      #   5 * 6 = 30
3 * 4 = 12      #   3 * 5 = 15
5 * 3 = 15      #   5 * 4 = 20
0 * 2 = 0       #   0 * 3 = 0
                    0 * 2 = 0

Usando dos mesmo calculos, se poder fazer um gerador de CPF valido.
'''

from random import randint

cpfgerado = str(randint(100000000, 999999999))
verificador_cpf = cpfgerado

reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(verificador_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        verificador_cpf += str(digito)

print(verificador_cpf)