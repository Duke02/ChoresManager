import typing

import util


class Housemate:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @staticmethod
    def from_json(json_obj: typing.Dict):
        name: str = json_obj["name"].strip()
        email: str = json_obj["email"].strip()
        if util.is_valid_email(email):
            print(f'WARNING: Email for {name} is not valid. Please check {email}.')
        return Housemate(name, email)
