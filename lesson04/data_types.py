"""Nesta aula falamos sobre tipos em python.
Tipos numéricos, inteiros, string etc.
Vimos algumas funções relacionados aos tipos.
Por mais informações e documentação sempre consultar o site
oficial do Python em https://python.org/docs

"""

# atribuições literiais
nome = "Eduardo"
sobrenome = "Moreira"

print(type(nome))
print(type(nome) == str)
print(isinstance(nome, str))

# concatenação de string
nome_completo = nome + " " + sobrenome
print(nome_completo)
nome_completo += "!"
print(nome_completo)

# inteiros
valor = 200
idade = int(70)
print(type(idade))
print(isinstance(idade, int))

# float
distancia = 20.89
pi = float(3.14)
print(type(distancia))
print(isinstance(pi, float))

# numeros complexos
num_complexos = 10+35j
print(type(num_complexos))
print(isinstance(num_complexos, complex))
print(num_complexos.real)
print(num_complexos.imag)