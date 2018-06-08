"""Enemy Class Module"""
class Enemy():
    """Base class for enemies

    Parameters
    ----------
    name : string
        The name of the enemy.
    hp : integer
        The enemy's health points
    damage : integer
        The enemy's damage value

    Attributes
    ----------
    name
    hp
    damage

    """
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        """check if enemy is still alive"""
        return self.hp > 0
