"""Nesta aula falamos sobre listas em python.
() ou tuple() é uma estrutura mutável.
Vimos algumas funções relacionados a estrutura de lista.

Por mais informações e documentação sempre consultar o site
oficial do Python em https://pyhon.org/docs

"""

uma_tuple = (1,3, "sorte")
print(uma_tuple)
outra_tupla = tuple(("Value", "Hoje"))
print(type(outra_tupla))

print(uma_tuple.count(9))
print(uma_tuple.index(3))

lista = list(uma_tuple)
lista.append("Alfredo")
print(lista)
nova_tuple = tuple(lista)

print(nova_tuple)

# descompactar
(x, *y, z) = nova_tuple
print(x)
print(y)
print(z)
