"""Nesta aula falamos sobre listas em python.
[] ou list() é uma estrutura mutável.
Vimos algumas funções relacionados a estrutura de lista.

Por mais informações e documentação sempre consultar o site
oficial do Python em https://pyhon.org/docs

"""

# definindo listas
clientes = ["Flávia", "Aline", "Silvia", "barbará"]
dados = ["Monica", 25, False]
list_vazia = []

# print("Aline" in clientes)
# print("Flávio" in clientes)

# print(clientes[0])
# print(clientes[-1])

# print(clientes.index("Silvia"))

# print(clientes[0:2])
# print(clientes[1:])
# print(clientes[-3:-1])

# print(len(clientes))

# adiconar elemeno no fim
# clientes.append("Vanessa")
# print(clientes)

# clientes += ["Pedro", "Gabriel"]
# print(clientes)

# clientes.extend(["João", "Matheus"])
# print(clientes)

# clientes.insert(0, "André")
# print(clientes)

# clientes[2:2] = ["Olivia", "Winie"]
# print(clientes)

# clientes[1:3] = ["Maçã", "Fruta"]
# print(clientes)

# clientes.remove("Aline")
# print(clientes)

# clientes.pop()
# print(clientes)

# del clientes[0]
# print(clientes)

# clientes.clear()
# print(clientes)

# clientes[1:2] = ["Fabiola"]
# print(clientes)

# print(clientes)
# clientes.sort(key=str.lower)
# print(clientes)

numeros = [2, 45, 67, 89, 1, 5]
# print(numeros)
# numeros.reverse()
# print(numeros)

# numeros.sort(reverse=True)
print(numeros)
print(sorted(numeros, reverse=True))
print(numeros)

copia_numeros = numeros.copy()
novos_numeros = list(numeros)
slice_numero = numeros[:]

print(type(novos_numeros))

