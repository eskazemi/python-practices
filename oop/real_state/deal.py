from base import Base


class Sell(Base):
    def __init__(self, price_per_meter, discountable, convertable,
                 *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.covertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"{self.price_per_meter}")


class Rant(Base):
    def __init__(self, initial_price, monthly_price, convertable, discountable
                 , *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.covertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)
