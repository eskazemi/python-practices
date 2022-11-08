from estate import Apartment, House, Store
from deal import Sell, Rant
from base import Base


class ApartmentSell(Apartment, Sell, Base):

    def show_detail(self):
        self.show_description()
        self.show_price()


class ApartmentRant(Apartment, Rant, Base):
    pass


class HouseSell(House, Sell, Base):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRant(House, Rant, Base):
    pass


class StoreSell(Store, Sell, Base):
    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreRant(Store, Rant, Base):
    pass
