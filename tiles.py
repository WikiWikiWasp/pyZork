import enemies, items

class MapTile:
    """This abstract MapTile class is going to provide a template for all of the tiles in the world.
    This abstract base class should not be used to instantiate any base maptile object. Use the specific subclass tiles instead

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
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and forboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass
