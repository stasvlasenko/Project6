#!/usr/bin/env python3

print("Content-type: text/html")
print()
print("<h1>Hello world!</h1>")

shaiba = 1
plastina = 2
gaika = 7
plastin = 9

shpilka = 0

loop = True
while loop == True:
    print('Введите количество пластин:')
    try:
        plastin = int(input())
    except ValueError:
        print('Вы ошиблись. Введено не число')
        continue


    shpilka = (gaika*2) + (shaiba*plastin + 1) + (plastin*plastina)
    print('Для образца из %s пластин, длина шпильки: %s мм' % (plastin, shpilka))