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

    print("__Percorrendo uma lista com o laço FOR__")
    lista = ["Raphael", "Santana", "Freitas", "Cazer"]
    print("Mostrando a lista completa:")
    print(lista)
    print("Separando os itens da lista")
    for mostra_lista in lista:
        print(mostra_lista)


def repeat_while():
    print(">>> Laço de repetição WHILE <<<")
    print()

    print("Diferentemente do laço FOR, é necessário declarar a variavel antes do laço e também declarar o passo dentro do laço")
    print("__Criando um contador de 1 a 10__")
    contador = 0
    # Variável declarada
    while contador <= 10:
        print(contador)
        contador += 1
        # Passo
    print()

    print("__Criando um contador de 10 a 1__")
    contador_inverso = 10
    while contador_inverso >= 0:
        print(contador_inverso)
        contador_inverso -= 1
        # Passo negativo


def sets():
    print(">>> Conjuntos <<<")
    print()

    print("__Criando um Conjunto__")
    print("Não é possivel ter dois elementos iguais (tipo e valor)")
    conjunto = {4, 9, 2, 1, 5,}
    # OBS PESSOAL: CONJUNTOS CRIADOS, SEMPRE VÃO SE ORGANIZAR DE FORMA AUTOMÁTICA
    print(conjunto)
    print()

    print("__Adcionando elementos ao Conjunto__")
    print("Conjunto original: {}".format(conjunto))
    conjunto.add(8)
    print("Conjunto após adição: {}".format(conjunto))
    print()

    print("__Remoção de elementos do Conjunto__")
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

    print("__União entre Conjuntos__")
    conjunto1 = {2, 4, 5, 8}
    conjunto2 = {1, 2, 7, 9}
    conjunto3 = conjunto1.union(conjunto2)
    print("Conjunto 1: {}".format(conjunto1))
    print("Conjunto 2: {}".format(conjunto2))
    print("A união dos Conjuntos: {}".format(conjunto3))
    # Respeitando a regra de não duplicidade, o conjunto não terá elementos repetidos
    print()

    print("__Interseção entre Conjuntos__")
    print("Apresenta os elementos que são comuns nos Conjuntos")
    conjuntoA = {1, 2, 4, 7, 9}
    conjuntoB = {3, 7, 1, 8, 5}
    conjuntoC = conjuntoB.intersection(conjuntoA)
    print("Conjunto A: {}".format(conjuntoA))
    print("Conjunto B: {}".format(conjuntoB))
    print("Interseção entre Conjuntos: {}".format(conjuntoC))
    # Respeita a regra de duplicidade e mostra apenas os elementos em comum em ambos os conjuntos
    print()

    print("__Diferença entre Conjuntos__")
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

    print("__Diferença Simétrica entre Conjuntos__")
    conjunto1 = {1, 4, 3, 5}
    conjunto2 = {1, 4, 6, 7}
    conjunto3 = conjunto2.symmetric_difference(conjunto1)
    # Cria um conjunto somente com os itens que não estão em ambos conjuntos
    print("Conjunto 1: {}".format(conjunto1))
    print("Conjunto 2: {}".format(conjunto2))
    print("Diferença simétrica entre os conjuntos: {}".format(conjunto3))
    print()

    print("__Subset__")
    conjuntoA = {1, 2, 4}
    conjuntoB = {1, 2, 7, 9, 4}
    conjuntoC = conjuntoA.issubset(conjuntoB)
    # Retorna True ou False, caso TODOS os elementos do Conjunto B façam parte do Conjunto A
    print("Conjunto A: {}".format(conjuntoA))
    print("Conjunto B: {}".format(conjuntoB))
    print("O conj.B tem todos os elementos do conj.A? {}".format(conjuntoC))
    print()

    print("__SuperSet__")
    conjuntoA = {1, 2, 4}
    conjuntoB = {1, 2, 7, 9, 4}
    conjuntoC = conjuntoA.issuperset(conjuntoB)
    # Retorna True ou False, caso TODOS os elementos do Conjunto B estejam no Conjunto A
    print("Conjunto A: {}".format(conjuntoA))
    print("Conjunto B: {}".format(conjuntoB))
    print("TODOS os elementos do conj.B estão no conj.A? {}".format(conjuntoC))


if __name__ == '__main__':
    sets()
