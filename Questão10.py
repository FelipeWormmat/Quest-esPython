class Funcionario:
    def __init__(self) -> None:
        self.nome = ""
        self.salario = 0
    
    def Salario(self):
        self.nome = input("Digite o nome do funcionário: ")
        self.salario = int(input("Digite o salário de {} : " .format(self.nome)))
        porcentagem  = int(input("Digite uma porcentagem: "))
        self.novo_salario = (self.salario * (porcentagem /100)) + self.salario
        return self.novo_salario

    def new_salario(self):
        print("O novo salario do {} é {}" .format(self.nome, self.novo_salario))

app = Funcionario()
app.Salario()
app.new_salario()