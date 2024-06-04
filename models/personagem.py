class Personagem:
    ATRIBUTOS_PADRAO = {
        'Guerreiro': {'inteligencia': 5, 'forca': 15, 'agilidade': 10,'vida_maxima':150},
        'Mago': {'inteligencia': 15, 'forca': 5, 'agilidade': 10,'vida_maxima': 100},
        'Arqueiro': {'inteligencia': 10, 'forca': 10, 'agilidade': 15,'vida_maxima':80},
    }

    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.inteligencia = Personagem.ATRIBUTOS_PADRAO[classe]['inteligencia']
        self.forca = Personagem.ATRIBUTOS_PADRAO[classe]['forca']
        self.agilidade = Personagem.ATRIBUTOS_PADRAO[classe]['agilidade']
        self.vida_maxima = Personagem.ATRIBUTOS_PADRAO[classe]['vida_maxima']
        self.inventario = []

    def curar(self,tamanho):
      if self.inventário:
          print('Inventário:')
          for item in self.inventario:
            print(f'- {item.nome} - {item.tamanho}')
      else:
        print('O inventário está vazio!') 
    
    def pegar_item(self, item):
      pass
    
    def atacar(self,monstro):
      pass
      
    def subir_nivel(self):
      pass
      
      
   