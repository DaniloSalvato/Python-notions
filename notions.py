# S - Single responsibility principle - Princípio de responsabilidade única
# O - Open/closed principle - Princípio aberto/fechado
# L - Liskov substitution principle - Princípio de substituição de Liskov
# I - Interface segregation principle - Princípio de segregação de interface
# D - Dependency inversion principle - Princípio de inversão de dependência

#Anotações POO python

#Criação de classe
class Exemplo:

    #metodo construtuor
    def __init__(self, atributo1):
        self.__atributo1 = atributo1

    #metodo da classe
    def exemplo_acao(self, novo_atributo):
        self.__atributo1 = self.__atributo1 + novo_atributo

    #metodo get
    @property
    def atributo(self):
        return self.__atributo1
    
    #metodo set
    @atributo.setter
    def atributo(self, atributo):
        self.__atributo1 = atributo

    #metodo static, não precisa ser instanciada a classe para ser acessado
    @staticmethod
    def static_method():
        return "metodo estatico"

#-------------------------------------------------------------------------------------------------------------------------------------
#Lista é uma coleção ordenada e mutável. Permite membros duplicados.
#Usa Index. Podemos utilizar [0],[1] para buscar informação, também funciona o contrario [-1] obs:(vai trazer o ultimo index)
lista = ["carro", True, 2, 3.5]
print(type(lista))

#lista.append("novo_elemento") 
# obs: adiciona um novo elemento no final

#del remove um elemento da lista de acordo com o index. 
# Ex: del lista [0]

#lista.remove("novo_elemento") 
#obs: função para remover o ele desejado

#lista = ["carro", True, 2, 3.5]
#lista[3] = 4.5
#obs: atribuição simples substitui um valor na posição desejada de index

#len(lista) 
#obs:lista o tamanho do array

#No python a string se comporta como lista então podemos acessa-lá facilmente
#string = Data
#print(string[0])

#-------------------------------------------------------------------------------------------------------------------------------------
#Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
#Usa Index
tupla = ("carro", True, 2, 3.5)
print(type(tupla))

#A tupla é muito parecida com a lista porém é formada por ()

#Caso a lista seja iniciada sem uma definição
#Ex: tupla = "carro", True, 2, 3.5 
#Ela automaticamente se torna uma tupla 

#-------------------------------------------------------------------------------------------------------------------------------------
#Dicionario é uma coleção ordenada e mutável. Não permite membros duplicados.
#Usa par chave valor
dicionario = {"nome": "carro", "logica": True, "numero": 2, "outro_numero": 3.5}
print(type(dicionario))

#Podemos acessar o valor de forma rápida procurando sua chave.
#Ex: dicionario["nome"]

#O dicionario tem tres funções importantes:

#dicionario.keys() 
#obs: retorna todas as chaves do dicionario
#dict_keys(['nome','logica', 'numero', 'outro_numero'])

#dicionario.values() 
#obs: retorna todas as valores do dicionario
#dict_keys(['carro','True', '2', '3.5'])

#dicionario.items() 
#obs: retorna lista de chave valor do dicionario
#dict_keys([('nome','carro'),('logica','True'), ('numero','2'), ('outro_numero','3.5')])

#Para deletar um item utilizamos o del passando o nome da chave 
#del dicionario["nome"]

#Para Alterar um item utilizamos passando o nome da chave passando o novo valor
#dicionario["nome"] = casa

#-------------------------------------------------------------------------------------------------------------------------------------
#Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
conjunto = {"carro", True, 2, 3.5}
print(type(conjunto))

#Se tentar criar um conjunto com elementos repetidos ele não vai dar erro,
#mas o elemento não é adicionado a repetição.
#Ex: conjunto = {"carro", True, true, 2, 2, 3.5} 
#resposta = {"carro", True, 2, 3.5}

#conjunto.add("novo_elemento")
#obs: adiciona um elemento ao conjunto porém ainda sem ordem. 

#elemento = conjunto.pop()
#obs: essa função vai retirar o item do conjunto e atribui-lo a outra variavel,
# porém o item vai ser excluido do conjunto, nesse caso quando não queremos que ele seja excluido 
# devemos converter o conjunto para lista primeiro e depois fazer as buscas.   


#-------------------------------------------------------------------------------------------------------------------------------------
#Conversão de coleções

lista = ["carro", True, 2, 3.5]
lista = tuple(lista)
lista = set(lista)

lista = dict([('carro','nissan'), ('casa','normal')])
print(lista)

#-------------------------------------------------------------------------------------------------------------------------------------
#Herança

#Quando um atributo é definido como privado ele passa a seguir o comportamento de "_nomeClasse__nomeAtributo",
#para trabalha com a herança precisamos alterar esse privado ("__") para somente um "_" que significa protegido por convesão 
#mas não o tornando privado. Ex: __atributo1 == _atributo1

class Mae:
    def __init__(self, atributo1):
        self._atributo1 = atributo1

    @property
    def atributo(self):
        return self._atributo1
    
    #metodo set
    @atributo.setter
    def atributo(self, atributo):
        self._atributo1 = atributo

#Quando colocado o parenteses na frente da classe indica a classe herdada
class Filho1(Mae):
    def __init__(self, atributo1, atributo2):
        #super().__init__ acessa os atributos que vão ser herdados da classe mãe
        super().__init__(atributo1)
        self.atributo2 = atributo2

class Filho2(Mae):
    def __init__(self, atributo1, atributo3):
        super().__init__(atributo1)
        self.atributo3 = atributo3

#Polimorfismo -> é a extensão da classe além da herança
a = Filho1(1, 2)
b = Filho2(1, 3)

lista = [a,b]

for item in lista:
    #Isso é um IF ternario que esta fazendo a verificação da existencia do atributo caso contrario ele retorno o da classe oposta
    detalhes = item.atributo2 if hasattr (item, 'atributo2') else item.atributo3
    print(f'{item.atributo}, {detalhes}')
        