from sample import create_sample
from advertisement import (
    ApartmentSell,
    ApartmentRant,
    HouseSell,
    HouseRant,
    StoreSell,
    StoreRant
)


class Handler:
    ADVERTISEMENT_TYPE = {
        1: ApartmentSell,
        2: ApartmentRant,
        3: HouseSell,
        4: HouseRant,
        5: StoreSell,
        6: StoreRant,
    }

    SWITCHES = {
        'r': 'get_report',
        's': 'show_all'
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            print(adv, adv.manager.count())


    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            print(adv, adv.manager.count())
            for obj in adv.object_list:
                obj.show_detail()


    def run(self):
        user_input = input("Enter Your choice ")
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print("invalid input")
            self.run()
        choice = getattr(self, switch, None)
        choice()


if __name__ == '__main__':
    create_sample()
    handler = Handler()
    handler.run()
