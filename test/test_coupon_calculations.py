import unittest
import store
from store.coupon_calculations import calculate_price


class TestCase(unittest.TestCase):

    def test_price_under_ten(self):
        self.calculateprice(6, 5, 10)
        self.calculate_price(6, 5, 15)
        self.calculate_price(6, 5, 20)
        self.calculate_price(6, 10, 10)
        self.calculate_price(6, 10, 15)
        self.calculate_price(6, 10, 20)

    def test_price_under_between_ten_thirty(self):
        self.calculate_price(15, 5, 10)
        self.calculate_price(15, 5, 15)
        self.calculate_price(15, 5, 20)
        self.calculate_price(15, 10, 10)
        self.calculate_price(15, 10, 15)
        self.calculate_price(15, 10, 20)
    def test_price_under_between_thirty_fifty(self):
        self.calculate_price(40, 5, 10)
        self.calculate_price(40, 5, 15)
        self.calculate_price(40, 5, 20)
        self.calculate_price(40, 10, 10)
        self.calculate_price(40, 10, 15)
        self.calculate_price(40, 10, 20)
    def test_price_under_over_fifty(self):
        self.calculate_price(70, 5, 10)
        self.calculate_price(70, 5, 15)
        self.calculate_price(70, 5, 20)
        self.calculate_price(70, 10, 10)
        self.calculate_price(70, 10, 15)
        self.calculate_price(70, 10, 20)


if __name__ == '__main__':
    unittest.main()
