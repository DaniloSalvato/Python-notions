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

#Polimorfismo -> é a extensão da clase além da herança
a = Filho1(1, 2)
b = Filho2(1, 3)

lista = [a,b]

for item in lista:
    #Isso é um IF ternario que esta fazendo a verificação da existencia do atributo caso contrario ele retorno o da classe oposta
    detalhes = item.atributo2 if hasattr (item, 'atributo2') else item.atributo3
    print(f'{item.atributo}, {detalhes}')