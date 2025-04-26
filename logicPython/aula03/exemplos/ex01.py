a = 5       # int
b = 3.14    # float
c= 2 + 3j   # complex

# Soma e atribuir: "+="
x = 5
x += 3  # equivalente a: x = x + 3 
print(x) # Saída: 8

# Subitrair e atribuir: "-="
x = 10
x -= 4  # equivalente a: x = x - 4 
print(x) # Saída: 6

# Multiplar e atribuir: "*="
x = 3
x *= 2  # equivalente a: x = x * 2
print(x) # Saída: 6

# Dividir e atribuir: "-="
x = 8
x /= 2  # equivalente a: x = x / 4 
print(x) # Saída: 4.0


#  Operações de Identidade

a = [1, 2,3]
b = a
print(a is b) # True -> 'a' e 'b' apontam para o mesmo objeto

a = [1, 2,3]
b = a
print(a is not b) # True -> 'a' e 'b' têm o mesmo, mas são objetos diferentes

# Operadores de Associação

frutas = ["maçã", "banana", "laranja"]
print("banana" in  frutas) # True (In -> significa se algo está contido)

frutas = ["maçã", "banana", "laranja"]
print("abacate" not in  frutas) # True (not in -> significa se algo não está contido)
