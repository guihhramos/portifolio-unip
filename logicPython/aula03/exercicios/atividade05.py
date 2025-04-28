print("Vamos calcular o crescimento do banco de dados!")

valor_inicial = 500  # em GB
taxa_crescimento = 0.08  # 8% ao mês
tempo = 6  # meses

valor_futuro = valor_inicial * (1 + taxa_crescimento) ** tempo

print(f"Após {tempo} meses, o banco de dados terá aproximadamente {valor_futuro:.2f} GB.")
