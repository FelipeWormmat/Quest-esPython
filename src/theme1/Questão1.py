def notas(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4
    

if __name__ == '__main__':
    media = notas(7,7,8,8)
    print (f'A nota do aluno seria: {media}')