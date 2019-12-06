import unittest
from part1_acme import Product, BoxingGlove
from part4_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flannability(self):
        """Test default product price being .05."""
        prod = Product('Test Product')
        self.assertEqual(prod.flannability, 0.5)

    def test_the_gloves(self):
        """Test glove price"""
        glove = BoxingGlove('A good puncher')
        self.assertEqual(glove.price, 100)

    def test_stealability(self):
        """stealable? """
        Anvil = Product('Acme Anvil', price=40, weight=100, flannibility=.1)
        self.assertEqual(Anvil.stealability(), "Not so stealable...")

    def test_stealability(self):
        """flammable? """


class AcmeReportTests(unittest.TestCase):
    """Making sure we make Acme products right."""

    def test_default_num_products(self):
        "30 products eh?"
        self.assertEqual(len(generate_products()), 30)


if __name__ == '__main__':
    unittest.main()
