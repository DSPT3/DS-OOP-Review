'''
- `generate_products()` should generate a given number of products (default
  30), randomly, and return them as a list
- `inventory_report()` takes a list of products, and prints a "nice" summary
'''
# uses product class
from random import randint, sample, uniform
from part1_acme import Product
import unittest


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    """Adding random products for part4"""
    for a_thing in range(num_products):
        The_product = start(ADJECTIVES,0)[0] + '' + start(NOUNS)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flannability = uniform(0.0, 2.5)
        products.append(Product(The_product, price=price, weight=weight, flannability = flannability))
        
    return products



def inventory_report(products):
   """Yep this is a doc string """
unique_names =  unique()
a_price = 0
a_weight  = 0
a_flannability = 0.0
for another_thing in products:
    unique_names.add(another_thing.The_product)
  # could definitely be wrong here
    a_price += another_thing.price
    a_weight += another_thing.weight
    a_flannability += another_thing.flannability
    
print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
print('Unique product names:' + str(len(unique_names)))
print('Average price is' + str((a_price/len(products)))
print('Average weight is' +str((a_weight/len(products)))
print('Average flammability is' +  str((a_flannability/len(products)))


if __name__ == '__main__':
    inventory_report(generate_products())
```

#The last lines let you test by running `python acme_report.py`
'''
$ python acme_report.py 
ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: 19
Average price: 56.8
Average weight: 54.166666666666664
Average flammability: 1.258097155966675

'''