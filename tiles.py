import enemies, items

class MapTile:
    """This abstract MapTile class is going to provide a template for all of the tiles in the world.
    Do not instantiate a base maptile object, use subclass tiles instead.

    Parameters
    ----------
    x : integer
        x-coordinate of the map.
    y : integer
        y-coordinate of the map.

    Attributes
    ----------
    x
    y

    """
    def __init__(self, x, y):
        """x-y corrdinates"""
        self.x = x
        self.y = y

    def intro_text(self):
        """displays some text to the user when they enter the new tile that
        descibes the world
        """
        raise NotImplementedError()

    def modify_player(self, player):
        """Moves player to new tiles"""
        raise NotImplementedError()


class StartingRoom(MapTile):
    """Starting room tile"""
    def intro_text(self):
        # this overrides the intro_text method of the base MapTile class
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and forboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        # needed to override to prevent superclass' modify_player from running
        pass


class LootRoom(MapTile):
    """Room tile that adds loot to player's inventory"""
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        """adds loot to player inventory"""
        player.inventory.append(self.item)

    def modify_player(self, player):
        """runs the add_loot method"""
        self.add_loot(player)


class EnemyRoom(MapTile):
    """Room tile with enemy encounter"""
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        """Player takes damage from enemy in room"""
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage.".format(self.enemy.damage))
            print("You have {} HP remaining.".format(player.hp))
