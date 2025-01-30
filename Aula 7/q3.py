# Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. O idioma é opcional e padrão para "inglês".
# função deve retornar uma saudação no idioma especificado.

def saudacao_personalizada(nome, idioma = "inglês"):
    if idioma == "inglês":
        return f"Hello,{nome}!"
    if idioma == "espanhol":
        return f"Hola, {nome}!"
    if idioma == "francês":
        return f"bonjour, {nome}!"

