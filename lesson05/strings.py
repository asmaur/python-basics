"""Nesta aula falamos sobre string em python.
Vimos algumas funções relacionados à string.
Por mais informações e documentação sempre consultar a site
oficial do Python em https://pyhon.org/docs

"""

nome = "Eduardo"
sobrenome = "Moreira"

# concatenação 
nome_completo = nome + " " + sobrenome
print(nome_completo)
nome_completo += "!"
print(nome_completo)

# multiplas linhas
frase = """
Oi, fábio.
Como você está?
"""
print(frase)

frase2 = "Oi, Ana.\nJá vou vou com o chefe.\nDeve ser a respeito daquele \"relatório\".\n\tObrigado por avisar!"
print(frase2)

# metodos de string
print(nome)
print(nome.lower())
print(nome.upper())
print(nome)

frase3 = "           Eu estou com sorte em 2024!                         "
print(len(frase3)) # inclui os espaços
print(len(frase3.strip()))
print(len(frase3.lstrip()))
print(len(frase3.rstrip()))

# indices
print(nome)
print(nome[1])
print(nome[-1])
print(nome[1:-1])
print(nome[:])

# metodos com retorno de booleano
print(nome.startswith("E"))
print(nome.startswith("e"))
print(nome.endswith("T"))

