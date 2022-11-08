from estate import Apartment, House, Store
from deal import Sell, Rant


class ApartmentSell(Apartment, Sell):

    def show_detail(self):
        self.show_description()
        self.show_price()


class ApartmentRant(Apartment, Rant):
    pass


class HouseSell(House, Sell):
    pass


class HouseRant(House, Rant):
    pass


class StoreSell(Store, Sell):
    pass


class StoreRant(Store, Rant):
    pass