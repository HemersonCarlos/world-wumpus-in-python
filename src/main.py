from movimentation_logic import Exploration
from knowledge_base import KnowledgeBase
from environment import WumpusWorld
from environment import size
#from view import ViewMatrix


class Main:

    print('\nGerando a configuração inicial do Mundo do Wumpus ' + str(size - 2) + 'x' + str(size - 2) + '...\n')
    world = WumpusWorld()

    print("\n\t MUNDO GERADO:")
    print('\n')
    for count in range(size):
        print(world.field[count])
    print('\n')
    for count in range(size):
        print(world.perceptions[count])

    base = KnowledgeBase(world)
    explore = Exploration(world, base)
    explore.move_agent()

    if explore.gold:
        print('\nOURO ENCONTRADO!')
    else:
        print('\nO agente NÃO CONSEGUIU encontrar o ouro!')

    print('\nPONTUAÇÃO: ' + str(explore.points) + '\n')

    #view = ViewMatrix()


if __name__ == '__main__':
    Main()