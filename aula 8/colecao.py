# Criando uma lista de números inteiros
lista_numeros = [10, 20, 30, 40, 50]

# Acessando elementos pelo índice
primeiro_elemento = lista_numeros[0]  # Resultado: 10
ultimo_elemento = lista_numeros[-1]   # Resultado: 50

# Modificando elementos
lista_numeros[2] = 35

# Adicionando elementos
lista_numeros.append(60)

# Removendo elementos
elemento_removido = lista_numeros.pop(1)  # Remove o elemento no índice 1 (20)

# Comprimento da lista
tamanho_da_lista = len(lista_numeros)  # Resultado: 5

# Exemplo 1: Criar uma lista de quadrados de números de 0 a 9
# Usando for loop:
quadrados = []
for num in range(10):
    quadrados.append(num ** 2)

# Usando list comprehension:
quadrados = [num ** 2 for num in range(10)]

# Exemplo 2: Filtrar apenas os números pares de uma lista
# Usando for loop:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

# Usando list comprehension:
pares = [num for num in numeros if num % 2 == 0]

# Exemplo 3: Converter letras para maiúsculas em uma lista de palavras
# Usando for loop:
palavras = ['python', 'é', 'incrível']
maiuculas = []
for palavra in palavras:
    maiuculas.append(palavra.upper())

# Usando list comprehension:
maiuculas = [palavra.upper() for palavra in palavras]

# Tuplas
# Uma tupla em Python é uma estrutura de dados semelhante a uma lista, mas com a diferença fundamental de ser imutável. 
# Isso significa que, uma vez que você cria uma tupla, não pode alterar, adicionar ou remover elementos dela. 
# A imutabilidade torna as tuplas mais seguras para armazenar dados que não devem ser modificados acidentalmente durante a execução do programa.

# Criando uma tupla de coordenadas (x, y)
ponto = (10, 20)

# Acessando elementos pelo índice
coordenada_x = ponto[0]  # Resultado: 10
coordenada_y = ponto[1]  # Resultado: 20

# Tentativa de modificar uma tupla (gerará um erro)
ponto[0] = 15  # Isso resultará em um TypeError, pois as tuplas são imutáveis

# Criando uma tupla com parênteses
tupla1 = (1, 2, 3)

# Criando uma tupla com a função tuple()
tupla2 = tuple([4, 5, 6])

tupla = (10, 20, 30, 40, 50)

primeiro_elemento = tupla[0]    # Resultado: 10
segundo_elemento = tupla[1]     # Resultado: 20
ultimo_elemento = tupla[-1]     # Resultado: 50

# Concatenação: É possível concatenar duas ou mais tuplas para formar uma nova tupla.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla_concatenada = tupla1 + tupla2  # Resultado: (1, 2, 3, 4, 5, 6)

# Multiplicação: Você pode multiplicar uma tupla por um inteiro para repetir seus elementos.
tupla = (1, 2, 3)

tupla_repetida = tupla * 3  # Resultado: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Utilidade das Tuplas
# As tuplas são úteis em várias situações, como:
# Retorno Múltiplo de Funções: Funções podem retornar múltiplos valores como uma tupla, permitindo que você desempacote os valores facilmente.
# Chaves de Dicionários: As tuplas são imutáveis e, portanto, podem ser usadas como chaves de dicionários.
# Necessidade de Imutabilidade: Quando você precisa garantir que os dados não serão alterados após a criação.

# Exemplo de retorno múltiplo de uma função
def calcular_valores(x, y):
    soma = x + y
    produto = x * y
    return soma, produto

resultado = calcular_valores(3, 5)  # Resultado: (8, 15)

# Desempacotamento dos valores retornados
soma_resultado, produto_resultado = resultado

# As tuplas são uma excelente opção quando você precisa armazenar uma coleção de valores que não mudarão e deseja garantir a integridade dos dados. 
# Elas complementam as listas e oferecem mais opções para manipulação de dados em Python.

# Criando um dicionário de informações de uma pessoa
pessoa = {
    'nome': 'João',
    'idade': 30,
    'profissão': 'Engenheiro'
}

# Acessando valores pelas chaves
nome_da_pessoa = pessoa['nome']   # Resultado: 'João'
idade_da_pessoa = pessoa['idade']  # Resultado: 30

# Modificando valores
pessoa['profissão'] = 'Desenvolvedor'

# Adicionando novos pares chave-valor
pessoa['cidade'] = 'São Paulo'

# Removendo um par chave-valor
del pessoa['idade']

# Mapeamento de Valores
# Suponha que queremos traduzir o nome de um dia da semana para outro idioma. Usando if-else, faríamos assim:

dia_da_semana = "Monday"

if dia_da_semana == "Monday":
    traducao = "Segunda-feira"
elif dia_da_semana == "Tuesday":
    traducao = "Terça-feira"
elif dia_da_semana == "Wednesday":
    traducao = "Quarta-feira"
# E assim por diante...
else:
    traducao = "Dia não encontrado"

print(traducao)  # Output: "Segunda-feira"

# Usando dicionário:

dia_da_semana = "Monday"

traducao_dias = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    # E assim por diante...
}

traducao = traducao_dias.get(dia_da_semana, "Dia não encontrado")
print(traducao)  # Output: "Segunda-feira"

# Execução de Funções Dinamicamente
# Outro cenário comum é executar funções com base em algum critério. Novamente, você pode usar dicionários para associar chaves a funções e, em seguida, executar a função correspondente com base nas chaves.

# Exemplo:
# Executando funções usando if-else
def saudacao_padrao():
    print("Olá!")

def saudacao_formal():
    print("Bom dia!")

def saudacao_informal():
    print("E aí!")

tipo_saudacao = "formal"

if tipo_saudacao == "padrao":
    saudacao_padrao()
elif tipo_saudacao == "formal":
    saudacao_formal()
elif tipo_saudacao == "informal":
    saudacao_informal()
else:
    print("Saudação desconhecida.")

# Usando dicionários:

# Executando funções usando dicionário
def saudacao_padrao():
    print("Olá!")

def saudacao_formal():
    print("Bom dia!")

def saudacao_informal():
    print("E aí!")

tipos_saudacao = {
    "padrao": saudacao_padrao,
    "formal": saudacao_formal,
    "informal": saudacao_informal
}

tipo_saudacao = "formal"

saudacao_func = tipos_saudacao.get(tipo_saudacao, None)
if saudacao_func:
    saudacao_func()
else:
    print("Saudação desconhecida.")