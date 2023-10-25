from stock import Stock
import unittest


class TestStock(unittest.TestCase):
    def test_create(self):
        name = "GOOG"
        shares = 101
        price = 35.99
        new_stock = Stock(name, shares, price)
        self.assertEqual(new_stock.name, name)
        self.assertEqual(new_stock.shares, shares)
        self.assertEqual(new_stock.price, price)

    def test_sell(self):
        name = "GOOG"
        shares = 101
        price = 35.99
        amount = 20
        new_stock = Stock(name, shares, price)
        new_stock.sell(amount)
        self.assertEqual(new_stock.shares + amount, shares)


if __name__ == "__main__":
    unittest.main()
