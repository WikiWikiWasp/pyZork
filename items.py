""" The base item class """
class Item():
    """The base class for all items

    Parameters
    ----------
    name : string
        The name of the item.
    desc : string
        The desc of the item.
    value : integer
        The value of the item.

    Attributes
    ----------
    name
    desc
    value

    """

    # constructor method
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

    # print method
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name,
                                                   self.desc,
                                                   self.value)

# Gold is now a subclass of the superclass Item
class Gold(Item):
    """Gold item class"""
    def __init__(self, amt):
        self.amt = amt
        # calls the superclass constructor
        # superclass constructor must always be called by a subclass constructor
        super().__init__(name='Gold',
                         desc='A round, golden coin',
                         value=self.amt)
        # uses the superclass's print method if not defined here


class Weapon(Item):
    """Base weapon class"""
    def __init__(self, name, desc, value, damage):
        self.damage = damage
        super().__init__(name, desc, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name,
                                                             self.desc, self.value, self.damage)


class Rock(Weapon):
    """Rock weapon class"""
    def __init__(self):
        super().__init__(name="Rock",
                         desc="A fist-sized rock, suitable for blugeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    """Dagger weapon class"""
    def __init__(self):
        super().__init__(name="Dagger",
                         desc="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=5)
