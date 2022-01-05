print()
print("Todos os código estão dentro de funções")
print("Utilizar o if_name para executar os códigos")
print()


def commands():
    print(">> Concatenação <<")
    print()
    print("É possivel concatenar de algumas formas:")

    variavel = "Variavel concatenada"
    print("1ºUso da virgula:")
    print("Essa frase contém uma concatenação ", variavel)
    # Após o fechamento da aspa, utiliza-se o , para implementar a variavel
    print("2ºUso do simbolo +:")
    print("Essa frase contém uma concatenação " + variavel)
    # Após o fechamento da aspa, utiliza-se o + para implementar a variavel
    print()
    print("Tópico especial para falar do .format()")
    # O .format() é uma forma facilitada e mais didática de implementar as variaveis
    print("Para utilizar o .format() será seguido algumas regras:")
    print("1ºUtilização dos {} dentro das aspas")
    # As chaves ficam dentro da frase para indicar onde a variavel vai ser implementada
    print("2º.format() será usado após as aspas")
    # Após o fechamento das aspas usa-se o .format(nome_da_variavel) para implementa-la
    nome = "Raphael"
    print("1ºExemplo: .format() com apenas uma variavel")
    print("Bem-Vindo {}".format(nome))
    idade = 24
    print("2ºExemplo: .format() com duas variavel")
    print("Olá {} você tem {} anos".format(nome, idade))
    cidade = "Salvador"
    print("3ºExemplo: declarando a variavel dentro do {} e as usando depois")
    print("Olá {name}, você é de {city} ?".format(name=nome, city=cidade))
    # Dentro das {} são denominados nomes para determinada variavel, que logo serão utilizadas no .format()


def basic_concepts():
    print(">>> Tipos Primitivos: <<<")
    print()
    nome = 'Raphael'
    print(nome)
    print("Tipo da variavel: {} ".format(type(nome)))
    # Conhecido também como STRINGS
    idade = 24
    print(idade)
    print("Tipo da variavel: {} ".format(type(idade)))
    # Conhecido também como INTEIROS
    altura = 1.73
    print(altura)
    print("Tipo da variavel: {} ".format(type(altura)))
    # Conhecido também como PONTO FLUTUANTE, ou seja, números com CASAS DECIMAIS
    ligado = True
    print(ligado)
    print("Tipo da variavel: {} ".format(type(ligado)))
    # Conhecido também como BOLEANOS (VERDADEIRO OU FALSO)


def arithmetics(a, b):
    print(">>> Tipos Aritméticos: <<<")
    print()
    print("VALORES: {} e {}".format(a, b))
    soma = a + b
    print("Soma: {}".format(soma))
    subtracao = a - b
    print("Subtração: {}".format(subtracao))
    divisao = a / b
    print("Divisão: {}".format(divisao))
    multplicacao = a * b
    print("Multiplicação: {}".format(multplicacao))
    resto = a % b
    print("Resto da divisão {}".format(resto))
    # Exemplo de resto de divisão: 2/5 = 2 e o resto é 1

    a = 10
    b = 12
    c = a < b
    print("__Menor que__ <")
    d = a > b
    print("__Maior que__ >")
    print("{} é menor que {}: {}".format(a, b, c))
    print("{} é maior que {}: {}".format(a, b, d))


def tuples_array():
    print(">>> Tuplas/Listas <<<")
    # Tuplas são criadas com () e Listas com []
    print()

    print("__Criando uma tuple:__")
    cores = ('Vermelho', 'Azul', 'Verde', 'Amarelo')
    print(cores)
    print("Tuplas são IMUTÁVEIS, ou seja, não podem ser modificadas")
    print("O tipo da variavel é: {}".format(type(cores)))
    print()

    print("__Encontrando Elementos:__")
    print("O elemento Azul está na posição {}".format(cores.index("Azul")))

    print("___Criando uma lista:___")
    pessoas = ['Raphael', 'Claudio', 'Lucas', 'Felipe', 'Amanda', 'Paula']
    print(pessoas)
    print()

    print("___Array Completo:___")
    print(pessoas)
    print("Este é o 3 elemento do Array: {}".format(pessoas[3]))
    print()

    print("___Ordenando elementos:___")
    print("Antes da Ordenação:")
    print(pessoas)
    pessoas.sort()
    print(pessoas)
    print("Revertendo a ordem dos elementos acima:")
    pessoas.sort(reverse=True)
    print(pessoas)
    print()

    print("___Excluindo elementos:___")
    print("Array Completo:")
    print(pessoas)
    pessoas.remove("Felipe")
    print("Excluindo um elemento pelo seu nome")
    print(pessoas)
    print("Excluindo o ultimo elemento")
    pessoas.pop()
    print(pessoas)
    print("Excluindo o indice 2")
    pessoas.pop(2)
    print(pessoas)
    print()

    print("__Alterando Elementos:__")
    print("Array Completo: ")
    print(pessoas)
    print("Alterando o Array:")
    pessoas[1] = "Dandara"
    print(pessoas)
    print()

    print("__Adcionando Elementos:__")
    print("Array Original:")
    print(pessoas)
    print("Alterando Array:")
    pessoas.append("Joo")
    print(pessoas)
    print()

    print("__Localizando um Elemento:__")
    elemento = pessoas.index("Joo")
    print("Localizando um elemento por sua referência")
    print("O elemento {} está na posição {}".format(pessoas[3], elemento))
    print()

    print("__Limpando uma Lista__")
    print("Array Completo:")
    print(pessoas)
    print("Limpando o Array:")
    pessoas.clear()
    print(pessoas)


def inputs():
    print(">> Entrada de usuário <<")
    print()

    print("__Inserindo Valores__")
    nome = input("Qual o seu nome? ")
    print("Olá {}, tudo bem?".format(nome))
    print()

    print("Valores inteiros precisam ser declarados antes")
    print("1ºExemplo: Sem declarar o tipo")
    numero1 = input("Digite um número inteiro: ")
    print("Digitado: {} e seu tipo é {}".format(numero1, type(numero1)))
    numero2 = int(input("Digite um número inteiro: "))
    print("Digitado: {} e seu tipo é {}".format(numero2, type(numero2)))
    print()

    print("Números do tipo FLOAT, precisa ser declarado antes também")
    float1 = input("Quanto vale pi? ")
    print("Pi vale {} seu tipo digitado foi {}".format(float1, type(float1)))
    float2 = float(input("Qual a temperatura de hoje? "))
    print("Hoje fazer {}ºC seu tipo digitado foi {}".format(float2, type(float2)))
    print()

    print("__Tratando Valores__")
    valor1 = int(input("Digite o 1º valor inteiro: "))
    valor2 = int(input("Digite o 2º valor inteiro: "))
    total = valor1 + valor2
    print("A soma entre {} e {} é igual a {}".format(valor1, valor2, total))


def simple_conditions(a, b):
    print(">>> Condicionais Simples <<<")
    print()

    print("__Condicional Simples: IF ELSE__")
    if a > b:
        print("Se {} for maior que {} então:".format(a, b))
        print("{} é maior que {}".format(a, b))
    else:
        print("Se {} for menor ou igual a {} então:".format(a, b))
        print("{} é menor ou igual a {}".format(a, b))
    print()

    print("__Condicional Simples: IF ELIF ELSE__")
    if a > b:
        print("{} é maior que {}".format(a, b))
    elif b > a:
        print("Elif é um else com condição")
        # Else if (condição):
        print("{} é maior que {}".format(b, a))
    else:
        print("{} é igual a {}".format(a, b))


def compose_conditions(a, b, c):
    print(">>> Condicionais Compostas <<<")
    print()

    print("__Mais de uma variável__")
    print("__ 3 Condições __")
    print("A: {} | B: {} | C: {}".format(a, b, c))
    if a + b + c > 10:
        print("A + B + C é MAIOR que 10")
    else:
        print("A + B + C é MENOR que 10")
    print()

    print("__Uso do operador AND__")
    # O operador AND só será validado se todas as condições forem VERDADEIRAS
    if (a + b > c) and (a + c > b) and (c + b > a):
        print("É um triângulo!")
    else:
        print("Não é um triângulo")
    print()

    print("__Uso do operador OR__")
    # O operador OR será validado caso alguma das condições for VERDADEIRA
    if (a == b) or (b == c) or (c == a):
        print("Algum dos valores é igual")
    else:
        print("Todos os valores são diferentes")
    print()

    print("__Uso do operador NOT__")
    # O operador NOT serve para negar algo que seria VERDEIRO, o tornando FALSO
    if (a > b) and not (b > c):
        print("A é maior que B e B NÃO é MAIOR que C ")
    else:
        print("B pode ser MAIOR que A e B é MAIOR QUE C")
    print()


if __name__ == '__main__':
    # Para executar qualquer um dos comandos, digitar o nome da função e executar
    # As funções arithmetics(2) | simple_conditions(2) | compose_conditions(3) necessitam de (x) parametros
    pass