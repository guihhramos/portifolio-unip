expressao = input("Digite a expressão algébrica: ")

expressao_formatada = expressao.replace("{", "(").replace("}", ")").replace("[", "(").replace("]", ")")

resultado = eval(expressao_formatada)

# Mostra o resultado
print(f"Resultado da expressão: {resultado}")

