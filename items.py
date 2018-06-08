""" The base item class """
class Item():
    """
    The base class for all items

    Parameters
    ----------
    name : string
        The name of the item.
    description : string
        The description of the item.
    value : integer
        The value of the item.

    Attributes
    ----------
    name
    description
    value

    """
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(
            self.name,
            self.description,
            self.value)
