def classes():
    print(">>> Classes and OBJECTS <<<")
    print()

    print("Python é uma linguagem orientada a objetos")
    # Quase tudo no python é um objeto, com propriedades e métodos
    print("Para criação de uma classes, é necessário a utilização da palavra reservada class (em minusculo)")
    print("Objeto é o item criado que utiliza as propriedades da classes")
    print()

    print("__ Criando uma CLASSE __")

    class valores:
        x = 5
        y = 9

    print(valores)
    # MOSTRANDO QUE A CLASSE FOI CRIADA

    p1 = valores()
    # VARIÁVEL QUE RECEBE A CLASSE
    print(p1)
    # O VALOR IMPRESSO É ONDE ELE SE LOCALIZA NA MEMÓRIA
    print()

    print("__ Criando uma classe com a função __init__ __")

    # A função init é um inicializador do objeto, ou seja, o que é necessário para que o objeto seja criado

    class Teste:
        def __init__(self, nome, idade):
            # self, é uma referência a instância atual que é utilizada para acessar as variáveis que pertecem a classe
            # O NOME NÃO PRECISA SER SELF, PODE SER QUALQUER NOME, USA-SE SELF POR CONVENÇÃO
            self.nome = nome
            self.idade = idade

        def diz_nome(self):
            print("My name is {}".format(self.nome))

    print()

    print("__ Criando um objeto e acessando as propriedades: __")
    jhon = Teste('Jhoony', 29)
    print("O nome do objeto jhon é {}".format(jhon.nome))
    print("A idade do objeto jhon é {} anos".format(jhon.idade))
    jhon.diz_nome()
    # Chamando a função dentro da classe
    print()

    print("__ Modificando as propriedades de um objeto: __")
    print("A antiga idade é {} anos".format(jhon.idade))
    jhon.idade = 32
    print("A nova idade de {} é {} anos".format(jhon.nome, jhon.idade))
    print()

    print("__ Deletando uma propriedade de um objeto: __")
    del jhon.nome
    # Após deletar a propriedade não é possível acessa-la lançando o erro AttributeError
    jhon.nome = "Jhonny"
    # Reatribuindo a propriedade nome
    del jhon
    # Também é possível deletar um objeto
    print()

    print("__ Criando uma classe Pai e Filho __")

    class Pessoa:
        def __init__(self, nome, idade, sexo):
            self.nome = nome
            self.idade = idade
            self.sexo = sexo

        def bemVindo(self):
            # Criando uma condição
            if self.sexo == 'F':
                print("Bem vinda Sra. {}, sua idade é {} anos".format(self.nome, self.idade))
            else:
                print("Bem vindo Sr. {}, sua idade é {} anos".format(self.nome, self.idade))

    class Professor(Pessoa):
        # Herda todas as características da classe Pessoa
        pass

    print("__: Chamando a Classe pai, com reescrita :__")

    class Estudante(Pessoa):
        # Herda a classe Pessoa
        def __init__(self, nome, sexo, idade, matricula):
            # Criar um método __init__ em uma classe filha, reescreve o método de inicialização desta classe, mas essa não é a única forma de adcionar um atributo a classe filha
            self.nome = nome
            self.sexo = sexo
            self.idade = idade
            self.matricula = matricula

    # Criando um objeto Pessoa
    catia = Pessoa("Catia", 53, 'F')
    vander = Pessoa("Vander", 60, 'M')
    catia.bemVindo()
    # Chamando a função
    vander.bemVindo()
    print()

    # Criando um objeto Professor, herdando a classe Pessoa
    fernanda = Professor('Fernanda', 32, 'F')
    paulo = Professor('Paulo', 29, 'M')
    fernanda.bemVindo()
    paulo.bemVindo()
    print()

    # Criando um objeto Estudante, sem herdar as característiscas da classe Pessoa
    rapha = Estudante('Raphael', 'M', 24, 7051997)
    # MATRICULA = 07051997 << O PYTHON NÃO ACEITA NÚMEROS COMEÇADOS COM 0
    rapha.bemVindo()
    print()

    print("__: Chamando a classe PAI, sem reescrever :__")

    class Funcionario(Pessoa):
        def __init__(self, nome, idade, sexo, funcao):
            # Criando o método __init__ na classe funcionário que recebe a classe PESSOA
            Pessoa.__init__(self, nome, idade, sexo)
            # Chamando a função __init__ da classe pai, dessa forma, não é preciso reescrever o método

            # OBS: É NECESSÁRIO COLOCAR TODOS OS PARÂMETROS DA CLASSE PAI NO __INIT__ DA CLASSE FILHO.
            self.funcao = funcao

        def fala_funcao(self):
            print(f"Olá {self.nome}, você é o {self.funcao} desta empresa")

    print()
    antonio = Funcionario('Antônio', 52, 'M', 'Diretor')
    antonio.bemVindo()

    class Responsaveis(Pessoa):
        def __init__(self, nome, idade, sexo, sobrenome):
            super().__init__(nome, idade, sexo)
            # No super() não se usa o self, porque o que está sendo intânciado é a classe filha, não a classe pai
            self.sobrenome = sobrenome

    maria = Responsaveis('Maria', 67, 'F', 'Santos')
    maria.bemVindo()
    print("__ É possível determinar os parâmetros com antecedência __")

    print()

    print("__: Método super() :__")

    class Loja():
        def __init__(self, nome, tamanho):
            self.nome = nome
            self.tamanho = tamanho

    class Weibon(Loja):
        def __init__(self, nome, tamanho):
            super().__init__(nome, tamanho)
            self.segmento = 'Moda'
            # Determinando um parâmetro antes, sem que seja necessário coloca-lo na hora da criação do objeto

        def diz_segmento(self):
            print(f"Sua loja está no segmento de {self.segmento}")

    dandara = Weibon('Loja da Weibon', 130)
    dandara.diz_segmento()
    dandara.segmento = 'Calçados'
    dandara.diz_segmento()


if __name__ == '__main__':
    classes()
