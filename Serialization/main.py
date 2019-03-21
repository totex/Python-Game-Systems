import pickle

game_new = False
game_restart = False


class Entity:
    def __init__(self, x, y, health, items, name):
        self.x = x
        self.y = y
        self.health = health
        self.items = items
        self.name = name

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def set_health(self, value):
        self.health = value

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    #def __str__(self):
    #    return '{} has {} health, its position is {}, and owns {}.'.format(self.name, self.health, self.get_position(), self.items)

    def __str__(self):
        return f'{self.name} has {self.health} health, its position is {self.get_position()}, and owns {self.items}.'


if game_new or game_restart:

    player = Entity(10, 10, 100, ['knife'], 'player')
    player.set_position(20, 10)
    player.set_health(80)
    player.add_item('sword')

    print(player.get_position())
    print(player.health)
    print(player.get_items())

    print('---------------------------')

    enemy = Entity(100, 10, 65, ['axe'], 'enemy')
    enemy.set_position(40, 10)
    enemy.set_health(55)
    enemy.remove_item('axe')

    print(enemy.get_position())
    print(enemy.health)
    print(enemy.get_items())

    print('------quitting and saving game------')
    # quitting the game, serialising the player and the enemy data
    with open('save_game.pkl', 'wb') as game_state_file:
        pickle.dump(player, game_state_file)
        pickle.dump(enemy, game_state_file)

else:
    print('------loading game------')
    with open('save_game.pkl', 'rb') as game_state_file:
        player = pickle.load(game_state_file)
        print(player)

        enemy = pickle.load(game_state_file)
        print(enemy)

