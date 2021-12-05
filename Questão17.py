def tabuada():
    numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    escolher_numero = int(input(f"Digite o numero que deseja da tabuada {numero}: "))

    for n in numero:
        print('{} X {} = {}'.format(escolher_numero, n , escolher_numero * n))

tabuada()