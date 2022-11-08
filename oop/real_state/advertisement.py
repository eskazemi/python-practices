from estate import Apartment, House, Store
from deal import Sell, Rant
from base import Base


class ApartmentSell(Apartment, Sell, Base):

    def show_detail(self):
        self.show_description()
        self.show_discountable()



class ApartmentRant(Apartment, Rant, Base):
    def show_detail(self):
        self.show_description()
        self.show_discountable()



class HouseSell(House, Sell, Base):
    def show_detail(self):
        self.show_description()
        self.show_discountable()


class HouseRant(House, Rant, Base):
    def show_detail(self):
        self.show_description()
        self.show_discountable()


class StoreSell(Store, Sell, Base):
    def show_detail(self):
        self.show_description()
        self.show_discountable()


class StoreRant(Store, Rant, Base):
    def show_detail(self):
        self.show_description()
        self.show_discountable()

