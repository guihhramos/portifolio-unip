# Receber o visitante 
print("Bem vindo viajante do tempo!")
print("Você está prestes a embarcar em uma jornada incrível...")
# Pedir as informações do visitante
nome = input("Qual é o seu nome viajante do tempo? ")

def obter_idade():
    while True:
        try:
            idade = int(input("Qual a sua idade? "))  # Tenta converter a entrada para inteiro
            if idade > 0:  # Verifica se a idade é positiva
                return idade  # Retorna a idade se for válida
            else:
                print("Idade inválida. Digite um número positivo.")
        except ValueError:  # Captura erros se a entrada não for um número inteiro
            print("Idade inválida. Digite um número inteiro.")

# Exemplo de uso
idade_viajante = obter_idade()

def obter_ano():
    while True:
        try:
            ano = int(input("Qual ano você veio? "))  # Tenta converter a entrada para inteiro
            if ano > 0:  # Verifica se a idade é positiva
                return ano  # Retorna a idade se for válida
            else:
                print("Ano inválida. Digite um número positivo.")
        except ValueError:  # Captura erros se a entrada não for um número inteiro
            print("Ano inválida. Digite um número positivo.")

# Exemplo de uso
ano_visitante = obter_ano()

# Saida
print("Nome do viajante: ", nome)
print("Idade do viajante:", idade_viajante)
print("Veio do ano: ", ano_visitante)
