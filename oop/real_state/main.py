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

if __name__ == '__main__':
    for mobile in MOBILE:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)
    r1 = Region(name="Azadi")
    apartment_sell = ApartmentSell(
        user=User.object_list[0], area=140, rooms_count=2,
        built_year=1399, region=r1, address="Tehran",
        has_parking=True, has_elevator=True, floor=5,
        price_per_meter=12000, convertable=False, discountable=True
    )
    apartment_sell.show_detail()
