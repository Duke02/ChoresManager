import typing
from datetime import date

import util
from chore import Chore
from housemate import Housemate


class ChoreOccurrence:

    def __init__(self, base_chore: Chore, happened: date, was_deep_clean: bool, cleaner: Housemate):
        self.base_chore = base_chore
        self.happened_on = happened
        self.was_deep_clean = was_deep_clean
        self.cleaner = cleaner

    def to_json(self) -> typing.Dict:
        return {'base_chore_key': self.base_chore.key,
                'happened_on': util.date_to_str(self.happened_on),
                'was_deep_clean': self.was_deep_clean,
                'cleaner_name': self.cleaner.name}

    @staticmethod
    def from_json(json_obj: typing.Dict, chores_listing: typing.List[Chore], housemates: typing.List[Housemate]):
        base_chore_key: str = json_obj["base_chore_key"]
        base_chore: Chore = filter(lambda c: c.key == base_chore_key, chores_listing)[0]
        happened_on: date = util.str_to_date(json_obj["happened_on"])
        was_deep_clean: bool = json_obj["was_deep_clean"]
        cleaner: Housemate = filter(lambda p: p.name == json_obj["cleaner_name"], housemates)[0]
        return ChoreOccurrence(base_chore, happened_on, was_deep_clean, cleaner)

    def __str__(self) -> str:
        return f'{self.base_chore}\n\tOn {util.date_to_str(self.happened_on)} by {self.cleaner.name}'
