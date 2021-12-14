class Aluno:

    def __init__(self, nt1, nt2):
        self.notas = [nt1, nt2]
    
    def calc_media(self) -> float:
        resultado = sum(self.notas)
        return resultado / (len(self.notas))

class Entrada:
    
    def __init__(self,alunos):
        self.alunos = alunos
    
    def cal_media_aluno(self):
        self.list_media = []
        for i in self.alunos:
            self.list_media.append(i.calc_media()) #lazy evaluation
    
    def seven(self):
        seven = []
        for i in self.list_media:
            if i >= 7:
                seven.append(i)
        return seven


    
class Escola:

    def alunos(self):
        i = 0
        list_aluno =[]
        while i < 5:
            nota1 = float(input("Nota 1 do aluno {}:  " .format(i+1)))
            nota2 = float(input("Nota 2 do aluno {}:  " .format(i+1)))
            
            list_aluno.append(Aluno(nota1,nota2))

            i += 1
        
    
        self._controler = Entrada(list_aluno)
    
    def qtd(self):
        self._controler.cal_media_aluno()
        qtd = self._controler.seven()
        print("a quantidade de alunos com média igual ou maior que 7 são {}" .format(len(qtd)))


api = Escola ()
api.alunos()
api.qtd()