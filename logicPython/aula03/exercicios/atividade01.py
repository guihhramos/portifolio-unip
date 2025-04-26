# Passo 0: Solicita uma frase ao usuário
frase = input("Digite sua frase secreta: ")

# Passo 1: Limpar espaços extras, normalizar e substituir palavras-chave
frase_limpa = frase.strip().lower()
frase_substituida = frase_limpa.replace("perigo", "risco").replace("encontro", "reunião")

# Passo 2: Inverter a string para esconder a mensagem
frase_invertida = frase_substituida[::-1]

# Passo 3: Mostrar a mensagem final criptografada
print("\n🔒 Sua mensagem secreta está pronta:")
print(frase_invertida)
