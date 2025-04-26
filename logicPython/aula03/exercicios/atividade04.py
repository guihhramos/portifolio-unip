# "Uma empresa de tecnologia gasta R$ 500,00 por 
# mês para manter X servidores. Se o custo mensal é de R$ 4.000,00,
# quantos servidores a empresa mantém?"
# R: 4.000/500

print("Vamos calcular a quantidade de servidores da sua empresa!")

valor1 = float(input("Digite o 1º valor (o valor que sua empresa gasta por servidor): "))
valor2 = float(input("Digite o 2º valor (o custo mensal total da empresa): "))

resultado = valor2 / valor1

print(f"O resultado é: {resultado}")
