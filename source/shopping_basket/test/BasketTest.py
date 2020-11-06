from unittest import TestCase

from Basket import Basket
from Item import Item


class BasketTest(TestCase):
    def test_empty_basket(self):
        basket = Basket([])
        self.assertEqual(0, basket.total())

    def test_single_item_quantity_one(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(100.0, basket.total())

    def test_two_items_quantity_one(self):
        basket = Basket([Item(200.0, 1), Item(100.0, 1)])
        self.assertEqual(300.00, basket.total())

    def test_single_item_quantity_two(self):
        basket = Basket([Item(100.0, 2)])
        self.assertEqual(200.0, basket.total())
