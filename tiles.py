import enemies, items

class MapTile:
    """The MapTile class is going to provide a template for all of the tiles
    in the world.

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
