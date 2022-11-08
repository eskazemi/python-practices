from user import User
from random import choice
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


def create_sample():
    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)
    r1 = Region(name="Azadi")
    apartment_sell = ApartmentSell(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        has_parking=True, has_elevator=True, floor=5,
        price_per_meter=12000, convertable=False, discountable=True
    )
    apartment_rant = ApartmentRant(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        has_parking=True, has_elevator=True, floor=5,
        initial_price=10000000,
        monthly_price=5000000
    )

    house_rant = HouseRant(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        has_yard=True, floors_count=3,
        initial_price=10000000,
        monthly_price=5000000
    )
    house_sell = HouseSell(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        has_yard=True, floors_count=3,
        price_per_meter=12000, convertable=False, discountable=True
    )
    store_sell = StoreSell(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        has_parking=True, has_elevator=True, floor=5,
        price_per_meter=12000, convertable=False, discountable=True
    )
    store_rent = StoreRant(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        initial_price=10000000,
        monthly_price=5000000
    )
    # print(apartment_sell.manager.search(region=r1)) print(
    # apartment_rant.manager.get(region=r1)) print(
    # apartment_rant.manager.search(rooms_count__min=3, rooms_count__max=4))
