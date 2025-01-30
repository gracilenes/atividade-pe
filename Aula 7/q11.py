# Escreva uma função em Python function que aceita uma string e retorna a quantidade de letras maiúsculas e minúsculas.
def contar_minusculas(texto: str):
    minusculas = 0
    for letra in texto:
        if letra.isalpha():
            if letra.upper() == letra:
                minusculas += 1
    return minusculas


def contar_maiusculas(texto: str):
    maiusculas = 0
    for letra in texto:
        if letra.isalpha():
            if letra.upper() == letra:
                maiusculas += 1
    return maiusculas

def contagem_letras(texto: str):
    maiusculas = 0
    minusculas = 0
    for letra in texto:
        if letra.isalpha():
            if letra.upper() == letra:
                maiusculas += 1
            elif letra.lower() == letra:
                minusculas += 1
    return maiusculas, minusculas

