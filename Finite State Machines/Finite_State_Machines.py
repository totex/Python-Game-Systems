from enum import Enum, auto
import time


class States(Enum):
    IDLE = auto()
    CHASE = auto()
    ATTACK = auto()
    DEATH = auto()


class GameObject:
    def __init__(self):
        self.__state = States.IDLE

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


class Entity(GameObject):
    def __init__(self):
        super().__init__()
        self.__health = 100

    def sub_health(self):
        self.__health -= 20

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health


player = Entity()
player.set_state(States.ATTACK)

enemy = Entity()
enemy.set_health(200)
enemy.set_state(States.CHASE)


while True:
    if player.get_state() == States.ATTACK:
        print("player attacking!")
        enemy.sub_health()
        if enemy.get_state() != States.ATTACK:
            enemy.set_state(States.ATTACK)
        if enemy.get_health() <= 0:
            enemy.set_state(States.DEATH)
            print("enemy died")
            print("proceed to next level")
            break
    elif player.get_state() == States.DEATH:
        print("player died")
        break
    if enemy.get_state() == States.ATTACK:
        print("enemy attacking!")
        player.sub_health()
        if player.get_health() <= 0:
            player.set_state(States.DEATH)
            print("player died")
            print("game over!")
            break

    time.sleep(1)

print("-----------------------------")
print("player's health ", player.get_health())
print("enemy's health", enemy.get_health())
