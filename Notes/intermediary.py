def repeat_for():
    print(">>> Laço de repetição FOR <<<")
    print()

    print("__Criando um contador de 1 a 10__")
    # Estrutura basica do for:
    # for variavel_criada in range(primeiro_elemento, ultimo_elemento, passo
    for laco in range(1, 10):
        print(laco)
        """
        O ultimo número sempre será o escolhido -1
        para que seja mostrado o 10, será necessário trocar o ultimo_elemento para 11
        """
    print()
    print("Por padrão, caso não seja declarado o passo, será adotado +1")
    print()

    print("__Criando um contador de 10 a 1__: ")
    for laco2 in range(10, 0, -1):
        # Neste caso o passo é declarado como -1
        # Seu último valor será 1
        print(laco2)
    print()

    print("__ Percorrendo uma lista com o laço FOR __")
    lista = ["Raphael", "Santana", "Freitas", "Cazer"]
    print("Mostrando a lista completa:")
    print(lista)
    print("Separando os itens da lista")
    for mostra_lista in lista:
        print(mostra_lista)
    print()

    print("__ Break / Continue __")
    print("1º Utilização do BREAK:")
    for cont in range(10):
        print(cont)
        if cont == 5:
            print("Fim!")
            break
            # Faz um pausa brusca, caso o cont seja igual a 5, o loop se encerra
    print("2º Utilização do CONTINUE:")

    for letras in 'Python':
        if letras == 'P':
            continue
            # Faz com que o próximo laço comece sem que passe para a próxima instrução
        print("Letra: {}".format(letras))


def repeat_while():
    print(">>> Laço de repetição WHILE <<<")
    print()

    print(
        "Diferentemente do laço FOR, é necessário declarar a variavel antes do laço e também declarar o passo dentro do laço")
    print("__ Criando um contador de 1 a 10 __")
    contador = 0
    # Variável declarada
    while contador <= 10:
        print(contador)
        contador += 1
        # Passo
    print()

    print("__ Criando um contador de 10 a 1 __")
    contador_inverso = 10
    while contador_inverso >= 0:
        print(contador_inverso)
        contador_inverso -= 1
        # Passo negativo


def sets():
    print(">>> Conjuntos <<<")
    # Conjuntos também são chamados de dicionários (dict)
    print()

    print("__ Criando um Conjunto __")
    print("Não é possivel ter dois elementos iguais (tipo e valor)")
    conjunto = {4, 9, 2, 1, 5, }
    # OBS PESSOAL: CONJUNTOS CRIADOS, SEMPRE VÃO SE ORGANIZAR DE FORMA AUTOMÁTICA
    print(conjunto)
    print()

    print("__ Adcionando elementos ao Conjunto __")
    print("Conjunto original: {}".format(conjunto))
    conjunto.add(8)
    print("Conjunto após adição: {}".format(conjunto))
    print()

    print("__ Remoção de elementos do Conjunto __")
    print("METODO 1:")
    print("Utilização do método remove(item)")
    print("Conjunto original: {}".format(conjunto))
    conjunto.remove(2)
    print("Conjunto após a remoção: {}".format(conjunto))
    print("METODO 2:")
    print("Utilização do método discart(item)")
    print("Conjunto original: {}".format(conjunto))
    conjunto.discard(5)
    print("Conjunto após a remoção: {}".format(conjunto))
    """
    Existe uma diferença entre os métodos remove e discard
    Remove: Caso o elemento esteja no conjunto o item é removido, caso contrário não é apresentado nenhum erro ou excessão
    Discard: Caso o elemento esteja no conjunto o item é removido, caso contrário é apresentado um erro informando que a operação não é possível.
    """
    print()

    print("__ União entre Conjuntos __")
    conjunto1 = {2, 4, 5, 8}
    conjunto2 = {1, 2, 7, 9}
    conjunto3 = conjunto1.union(conjunto2)
    print("Conjunto 1: {}".format(conjunto1))
    print("Conjunto 2: {}".format(conjunto2))
    print("A união dos Conjuntos: {}".format(conjunto3))
    # Respeitando a regra de não duplicidade, o conjunto não terá elementos repetidos
    print()

    print("__ Interseção entre Conjuntos __")
    print("Apresenta os elementos que são comuns nos Conjuntos")
    conjuntoA = {1, 2, 4, 7, 9}
    conjuntoB = {3, 7, 1, 8, 5}
    conjuntoC = conjuntoB.intersection(conjuntoA)
    print("Conjunto A: {}".format(conjuntoA))
    print("Conjunto B: {}".format(conjuntoB))
    print("Interseção entre Conjuntos: {}".format(conjuntoC))
    # Respeita a regra de duplicidade e mostra apenas os elementos em comum em ambos os conjuntos
    print()

    print("__ Diferença entre Conjuntos __")
    conjuntoI = {1, 2, 4, 6, 8}
    conjuntoII = {3, 5, 1, 4, 6}
    conjuntoIII = conjuntoI.difference(conjuntoII)
    # Criando um conjunto com as diferenças entre o I e o II
    conjuntoIV = conjuntoII.difference(conjuntoI)
    # Criando um conjunto com as diferenças entre o II e o I
    print("Conjunto I: {}".format(conjuntoI))
    print("Conjunto II: {}".format(conjuntoII))
    print("Diferença do conjunto I para o II: {}".format(conjuntoIII))
    print("Diferença do conjunto II para o I: {}".format(conjuntoIV))
    print()

    print("__ Diferença Simétrica entre Conjuntos __")
    conjunto1 = {1, 4, 3, 5}
    conjunto2 = {1, 4, 6, 7}
    conjunto3 = conjunto2.symmetric_difference(conjunto1)
    # Cria um conjunto somente com os itens que não estão em ambos conjuntos
    print("Conjunto 1: {}".format(conjunto1))
    print("Conjunto 2: {}".format(conjunto2))
    print("Diferença simétrica entre os conjuntos: {}".format(conjunto3))
    print()

    print("__ Subset __")
    conjuntoA = {1, 2, 4}
    conjuntoB = {1, 2, 7, 9, 4}
    conjuntoC = conjuntoA.issubset(conjuntoB)
    # Retorna True ou False, caso TODOS os elementos do Conjunto B façam parte do Conjunto A
    print("Conjunto A: {}".format(conjuntoA))
    print("Conjunto B: {}".format(conjuntoB))
    print("O conj.B tem todos os elementos do conj.A? {}".format(conjuntoC))
    print()

    print("__ SuperSet __")
    conjuntoA = {1, 2, 4}
    conjuntoB = {1, 2, 7, 9, 4}
    conjuntoC = conjuntoA.issuperset(conjuntoB)
    # Retorna True ou False, caso TODOS os elementos do Conjunto B estejam no Conjunto A
    print("Conjunto A: {}".format(conjuntoA))
    print("Conjunto B: {}".format(conjuntoB))
    print("TODOS os elementos do conj.B estão no conj.A? {}".format(conjuntoC))


def function():
    print(">>> Definitions <<<")
    print()

    print("__ Criando uma Função __")
    print("Toda função no python começa com def nome_funcao()")
    print("Checar os comentários")
    """"
    Os () indicam se a função receberá algum valor
    Por exemplo:
    def soma(a,b): # Explicando: A função receberá 2 parametros
        total = a + b # Explicando: Os 2 parametros serão somados 
        return total    # A função irá retornar o resultado
    Chamando a função acima:
    print(soma(10, 2)) # Explicando: Forma de chamar a função e imprimindo
    """
    print()

    print("Existem diversas vantagens de usar as funções / definições")
    print("1º Conseguir dividir seu código em pequenos trechos")
    print("1.1º Códigos divididos são mais fáceis para refatorar")
    print("1.2º É possível executar partes separadas do código")
    print("2º Toda aplicação é feita em funções")


def transform_list_dict():
    print(">>> Transformação de Arrays e Set <<<")
    print()

    print("__ Conjunto para Lista __")
    conjunto = {"Raphael", "Vanessa", "Dona Joo"}
    print("Este é o set: {}".format(conjunto))
    print("Tipo da variável: {}".format(type(conjunto)))
    lista = list(conjunto)
    print("Váriavel após a transformação: {}".format(lista))
    print("Tipo da variável: {}".format(type(lista)))
    print()

    print("__ Lista para Conjuntos __")
    lista = [1, 2, 3, 4, 5, 5]
    print("Está é a lista: {}".format(lista))
    print("Tipo da variável: {}".format(type(lista)))
    conjunto = set(lista)
    print("Variavel após transformação: {}".format(conjunto))
    print("Tipo da variável: {}".format(type(conjunto)))


def advanced_strings():
    print(">>> Conceitos avançado sobre Strings <<<")
    print()

    print("__ Multiplas linhas __")
    # Ao utilizar """ texto """ aspas triplas (simples ou duplas) é possivel escrever varias linhas
    linhas = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut posuere nunc sed tortor tempor, ut blandit arcu placerat. Nam risus diam, condimentum vitae urna eu, porttitor ornare velit. Pellentesque sed velit risus. Morbi varius aliquet aliquam. Suspendisse at mattis neque. """
    print(linhas)
    print()

    print("__ Strings são listas __")
    hello = 'HELLO WORLD'
    print("Escolhendo a posição: {}".format(hello[3]))
    # String são arrays, por isso é possivel escolher a posição deseja mostrar
    print("É possível utilizar o FOR dentro de uma string:")
    fruta = 'tomate'
    for letras in fruta:
        print(letras)
    print("1º É possível saber seu tamanho:")
    palavra = 'onomatopeia'
    print("A palavra {} tem {} letras".format(palavra, len(palavra)))
    print("2º Checar se há tal elemento dentro da string:")
    # Lembrando que é case sensite, ou seja, há diferença entre maiúsculo e minusculo
    string = "Aqui temos um exemplo de string, para checagem"
    print("A frase é: {}".format(string))
    print("A palavra OK está na variavel: {}".format("Ok" in string))
    print("A palavra temos está na variavel: {}".format("temos" in string))
    print("3º Checar se NÃO há tal elemento dentro da sting:")
    print("Retorna False se encontrar e True se NÃO encontrar")
    stringnot = "Mais um exemplo de string para checagem"
    print("A frase é: {}".format(stringnot))
    print("A palavra exemplo está na variavel: {}".format("exemplo" not in string))
    print()

    print("__ \"Recortando\" Strings __ ")
    ola = 'Olá Mundo!'
    print("String original: {}".format(ola))
    print("Parte da string: {}".format(ola[0:3]))
    # variavel[posicao_inicial : posicao_final]
    print("Partido do início e indo até certa posição:")
    inicio = "Tudo bem?"
    print("String original: {}".format(inicio))
    print("Parte da string: {}".format(inicio[:4]))
    # Outra forma: variavel[0:4]
    print("Escolhendo o ponto inicial e indo até o final:")
    final = "Aqui estou mais um dia"
    print("String original: {}".format(final))
    print("String original: {}".format(final[5:]))
    # Escolhe a posição inicial e vai até o final
    print()

    print("__ Transformando Strings __")
    minuscula = 'OLÁ MUNDO!'
    print("1º Minuscula:")
    print("String Original: {}".format(minuscula))
    print("Em minúscula: {}".format(minuscula.lower()))
    # .chamando a função lower() que transforma a string toda em minuscula
    print("2º Maiúscula:")
    maiuscula = 'hello world!'
    print("String Original: {}".format(maiuscula))
    print("Em minúscula: {}".format(maiuscula.upper()))
    print("3º Primeira letra maiúscula:")
    primeiraLetra = 'OLA WORLD!'
    print("String Original: {}".format(primeiraLetra))
    print("String modificada: {}".format(primeiraLetra.capitalize()))
    # Somente a primeira letra da string estará em maiusculo
    print()

    print("__ Outros métodos __")
    print("Remover espaços em branco: ")
    branco = '  Espaços  '
    print("String Original: {}".format(branco))
    print("Tamanho da String: {}".format(len(branco)))
    removeBranco = branco.strip()
    print("String sem espaços em branco: {}".format(removeBranco))
    print("Novo tamanho da String: {}".format(len(removeBranco)))
    print()

    print("Substituição:")
    string1 = 'Hello World!'
    print("String Original: {}".format(string1))
    string2 = string1.replace('l', 'u')
    # Trocando todas as letra l por u
    print("Trocando o l por t: {}".format(string2))
    print()

    print("Dividindo a String:")
    original = 'Tudo bem contigo?'
    print("String original: {}".format(original))
    dividido = original.split(" ")
    # split(" "), a divisão é por espaços em branco
    print("Nova String: {}".format(dividido))
    print()

    print("Métodos de Pesquisa:")
    pesquisa = 'Welcome to the jungle!'
    print("Método find():")
    procura = pesquisa.find('to')
    # Retorna onde começa o elemeto a ser pesquisado
    # Caso não encontre retorna -1
    print("Indicando a posição INICIAL da busca: {}".format(procura))
    print("Método index():")
    pesquisa2 = 'Welcome to the prision'
    procura2 = pesquisa2.index('the')
    # Retorna onde começa o elemeto a ser pesquisado
    # Caso não encontre lança um erro "ValueError: substring not found"
    print("Indicando a posição INICIAL da busca: {}".format(procura2))


def lambdas():
    print(">>> LAMBDAS <<<")
    print()
    # Funções lambdas, também conhecidas como funções anônimas são uma forma de simplificar algumas funções.
    # NÃO É OBRIGATÓRIO USAR FUNÇÕES ANÔNIMAS, PORÉM UTILIZA-LAS TORNA O CÓDIGO MAIS LIMPO

    print("""FUNÇÃO COMUM:
    def multiplicacao(a, b):
        total = a * b
        return total
    """)

    print("""FUNÇÃO LAMBDA:
    multiplicacao = lambda a, b: a * b""")


if __name__ == '__main__':
    pass