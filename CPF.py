'''
Validando um CPF.
CPF = 168.995.350-09
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

    297              #      343
11 - (297 % 11) = 11 #   11 - (343 % 11) = 9
11 > 9 = 0           #
                     #
Digito 1 = 0               digito 2 = 9
'''

CPF = '168.995.350-09'
novo = []

for x in CPF[0:11]:
    if not x.isnumeric():
        ...
    else:
        novo += x

list2 = []
mult1 = 10

for x in novo:
    cal = int(x) * mult1
    list2.append(cal)
    mult1 = mult1 - 1
ad = 0
for x in list2:
    ad = ad + int(x)

part1 = 11 - (ad % 11)
if part1 >= 9:
    part1 = 0
    novo.append(part1)

list3 = []
mult2 = 11
for x in novo:
    cal = int(x) * mult2
    list3.append(cal)
    mult2 = mult2 - 1

ad2 = 0
for x in list3:
    ad2 = int(x)+ad2

part2 = 11-(ad2 % 11)
if part2 >= 9:
    novo.append(part2)

novo_cpf = ''
for x in novo:
    novo_cpf += str(x)
print(novo_cpf)
remove = ', . -'
comparacao = CPF.translate(str.maketrans('', '', remove))

if comparacao == novo_cpf:
    print('Esse CPF é válido!')
else:
    print('Esse CPF não é valido!')