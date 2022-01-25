import unittest
from ocp import *


class TestCart(unittest.TestCase):

    def setUp(self):
        self.food = Cart()
        self.laptop = Cart()

    def test_food(self):
        self.assertEqual(
            self.food(PriceRuleFood, 3, 100), 300
            )

    def test_laptop(self):
        self.assertEqual(
            self.laptop(PriceRuleLapTop, 5, 1000), 4000
        )