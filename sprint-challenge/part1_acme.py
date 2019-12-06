"""
make classes here 
"""

from random import randint
import unittest


class Product:
    "part 1 stuff here "

    def __init__(self, name, price=10, weight=20, flannability=.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flannability = flannability
        self.identifier = randint(1000000, 9999999)

        # part 2
    def stealability(self):
        """METhods for part 2, first one is  - calculates the price divided by the weight, and then
  returns a message: if the ratio is less than 0.5 return Not so stealable...,
  if it is greater or equal to 0.5 but less than 1.0 return Kinda stealable.,
  and otherwise return Very stealable! """

        Price_weight = self.price / self.weight
        if Price_weight < .05:
            return "Not so stealable..."
        elif Price_weight < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable'

    def explode(self):
        """Second method is  - calculates the flammability times the weight, and then
  returns a message: if the product is less than 10 return ...fizzle., if it is
  greater or equal to 10 but less than 50 return ...boom!, and otherwise
  return ...BABOOM!!"""
        fire_potential = self.flannability * self.weight
        if fire_potential < 10:
            return '...fizzle'
        elif fire_potential < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

        # part 3 sublass


class BoxingGlove(Product):
    """Subclass for the class parent. - Change the default `weight` to 10 (but leave other defaults unchanged)
- Override the `explode` method to always return ...it's a glove.
- Add a `punch` method that returns "That tickles." if the weight is below 5,
  Hey that hurt! 
  if the weight is greater or equal to 5 but less than 15, and
  OUCH! otherwise
  """

    def __init__(self, name, price=100, weight=10, flannability=.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flannability = flannability
        self.identifier = randint(1000000, 9999999)
        # change the price for giggles, and did not work. further investagation needed.

    def explode(self):
       # """A doc string needs to be here?Nah"""
        return "...it's a glove."

    def punch(self):
        # you are not working, futher investagtion needed...
        """a method of a BoxingGLove"""
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
