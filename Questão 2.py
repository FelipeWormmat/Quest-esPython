from typing import List

class Entrada:
    def __init__(self, entrada):
        self.entrada = entrada
        self.consantes: List[str] = self._separaconsoantes(self.entrada)

    def _separaconsoantes(self, entrada) -> List[str]:
        entrada.lower()
        consoantes: List[str] = []
        for caractere in entrada:
            if(caractere) not in ('a','e','i','o','u',' '):
                consoantes.append(caractere)
        return consoantes


class Frase:
    entrada = Entrada(input('Digite sua frase: '))
    print(entrada.consantes)
    print(len(entrada.consantes))