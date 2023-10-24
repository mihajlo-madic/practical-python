from typedproperty import String, Int, Float


class Stock:
    """
    Made for representing stock datatype
    """

    name = String("name")
    shares = Int("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        """
        Returns current value of a stock
        """
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount
        return amount * self.price

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"
