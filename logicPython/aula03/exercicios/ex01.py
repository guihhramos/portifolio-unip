
from statistics import mean, median, multimode

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class RelacaoFuncionarios:
    def __init__(self):
        self.lista_funcionarios = []

    def adicionar_funcionario(self, nome, cargo, salario_str):
        salario = float(salario_str.replace("R$", "").replace(".", "").replace(",", "."))
        funcionario = Funcionario(nome, cargo, salario)
        self.lista_funcionarios.append(funcionario)

    def calcular_media_salarial(self):
        salarios = [f.salario for f in self.lista_funcionarios]
        return round(mean(salarios), 2)

    def calcular_mediana_salarial(self):
        salarios = [f.salario for f in self.lista_funcionarios]
        return round(median(salarios), 2)

    def calcular_moda_salarial(self):
        salarios = [f.salario for f in self.lista_funcionarios]
        modas = multimode(salarios)
        return [round(m, 2) for m in modas]

    def exibir_resultados(self):
        print(f"Média Salarial: R$ {self.calcular_media_salarial():,.2f}".replace(".", ","))
        print(f"Mediana Salarial: R$ {self.calcular_mediana_salarial():,.2f}".replace(".", ","))
        modas = self.calcular_moda_salarial()
        moda_formatada = " - ".join(f"R$ {m:,.2f}".replace(".", ",") for m in modas)
        print(f"Moda Salarial: {moda_formatada}")

# Criar objeto da relação de funcionários
relacao = RelacaoFuncionarios()

# Adicionar funcionários
relacao.adicionar_funcionario("ZEQUINHA DA SILVA", "DESENVOLVEDOR JR", "R$ 5.800,00")
relacao.adicionar_funcionario("TONHO DA SILVA", "DESENVOLVEDOR PLENO", "R$ 7.250,00")
relacao.adicionar_funcionario("EZEQUIEL DA SILVA", "DESENVOLVEDOR SENIOR", "R$ 9.320,00")
relacao.adicionar_funcionario("VANDER DOS SANTOS", "DESENVOLVEDOR JR", "R$ 5.800,00")
relacao.adicionar_funcionario("ARICLENILDO DOS SANTOS", "DESENVOLVEDOR PLENO", "R$ 7.250,00")

# Exibir resultados
relacao.exibir_resultados()
