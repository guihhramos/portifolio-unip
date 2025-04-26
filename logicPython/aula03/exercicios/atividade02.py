import datetime

# Passo 0: Obter o ano atual (automaticamente)
ano_actual = datetime.datetime.now().year
print(f"Ano atual detectado: {ano_actual}")

# Também dá opção para o usuário digitar outro ano atual, se quiser
usar_ano_manual = input("Deseja inserir o ano atual manualmente? (s/n): ").lower()
if usar_ano_manual == "s":
    ano_actual = int(input("Digite o ano atual: "))

# Solicita o ano de destino
ano_destino = int(input("Digite o ano de destino: "))

# Passo 1: Calcular a diferença entre os anos
diferenca = ano_destino - ano_actual

# Mostrar a diferença
if diferenca > 0:
    print(f"Você vai viajar {diferenca} anos para o futuro!")
elif diferenca < 0:
    print(f"Você vai viajar {abs(diferenca)} anos para o passado!")
else:
    print("Você está no presente!")

# Passo 2: Determinar década e século do ano de destino
decada = (ano_destino // 10) * 10
seculo = (ano_destino - 1) // 100 + 1  # Ex: 2025 => século 21

print(f"O ano {ano_destino} pertence à década de {decada} e ao século {seculo}.")

# Mensagem divertida opcional
print("🕓 Salto temporal calculado com sucesso! 🚀")
