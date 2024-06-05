from models.items.item import Pocao,Arma, Espada, Arco, Cajado
from models.personagem import Personagem
from models.monstros.monstro import Monstro

def main():
    # Criando um personagem
    personagem = Personagem("Aragorn", "Guerreiro")

    # Criando um monstro
    monstro = Monstro("Orc", 50)

    # Criando alguns itens
    pocao = Pocao("Poção de Cura", "medio", 30)
    espada = Espada("Espada Longa", "grande", 25)
    arco = Arco("Arco Longo", "grande", 20)
    cajado = Cajado("Cajado Mágico", "medio", 15)

    # Adicionando itens ao inventário do personagem
    personagem.adicionar_item(pocao)
    personagem.adicionar_item(espada)
    personagem.adicionar_item(arco)
    personagem.adicionar_item(cajado)

    # Mostrando o inventário do personagem
    personagem.mostrar_inventario()

    # Atacando o monstro
    personagem.atacar(monstro)
    