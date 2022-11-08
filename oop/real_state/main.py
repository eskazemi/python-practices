from user import User
from random import choice
from estate import Apartment, House, Store
from region import Region
from advertisement import (
    ApartmentSell,
    ApartmentRant,
    HouseSell,
    HouseRant,
    StoreSell,
    StoreRant
)

FIRST_NAME = ["Ali", "Hasan", "Karim"]
LAST_NAME = ["Hasani", "Kazemi", "Kamali"]
MOBILE = ["09032356897", "0907818262", "09121012525"]

if __name__ == '__main__':
    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    print(len(User.object_list))
    for user in User.object_list:
        print(user.id, user.fullname)

    r1 = Region(name="Azadi")
    apt1 = Apartment(user=User.object_list[0], area=140, rooms_count=2,
                     built_year=1399, region=r1, address="Tehran",
                     has_parking=True, has_elevator=True, floor=5,
                     )
    apt1.show_description()

    house = House(user=User.object_list[1], area=120, rooms_count=3,
                  built_year=1400, region=r1, address="Tehran", has_yard=True,
                  floors_count=2)

    house.show_description()

    store_1 = Store(user=User.object_list[2], area=40, rooms_count=0,
                    built_year=1400, region=r1, address="Tehran")

    store_1.show_description()

    apartment_sell = ApartmentSell(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        has_parking=True, has_elevator=True, floor=5,
        price_per_meter=12000, convertable=False, discountable=True
    )
    apartment_sell.show_detail()
    print(ApartmentSell.mro())
