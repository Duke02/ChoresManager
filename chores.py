import json
import typing

from chore import Chore
from housemate import Housemate


def get_chores(filepath: str = 'chores.json') -> typing.List[Chore]:
    """
    Loads the chores from the specified file path and returns the loaded files.
    :param filepath: The json file holding the chores that are currently in the system.
    :return: The listing of chores within the file.
    """
    print(f'Loading chores from {filepath}...')
    chores: typing.List[Chore] = []
    with open(filepath, 'r') as f:
        chores = [Chore.from_json(obj) for obj in json.load(f)]

    print(f'Loaded {len(chores)} from {filepath}.')
    return chores


def print_chores(chores: typing.List[Chore]):
    """
    Prints the given chores.
    :param chores: The chores to print.
    """
    for index, chore in enumerate(chores):
        print(f'{index + 1:3}. {chore.key:3} \'{chore.name}\'')


def save_chores(chores: typing.List[Chore], filepath: str = 'chores.json'):
    """
    Saves the provided chores to the given filepath.
    :param chores: The chores to save.
    :param filepath: The path to the json file to save chores in.
    """
    print(f'Saving {len(chores)} chores to {filepath}...')
    with open(filepath, 'w') as f:
        json.dump([chore.__dict__ for chore in chores], f)
    print(f'Finished saving chores to {filepath}.')


def get_chores_from_user(existing_chores: typing.List[Chore]) -> typing.List[Chore]:
    """
    Adds any chores from the user through an interactive process.
    :param existing_chores: The chores that are already in the system.
    :return: The existing chores and any new chores that were provided by the user.
    """
    print('These are the existing chores:')
    print_chores(existing_chores)

    user_wants_to_add: bool = input('Is there any that you would like to add? (y/n) ').lower() == 'y'

    if not user_wants_to_add:
        print('Okay, will not add any chores.')
        return existing_chores

    while user_wants_to_add:
        name: str = input('What is the name of the chore? ').title()
        key: str = input('What should the key be? (2 characters) ').upper()
        description: str = input('What should someone do if they were doing the chore? ')
        has_deep_clean: bool = input('Is there a deep clean option for the chore? (y/n) ').lower() == 'y'
        deep_clean: str = '' if not has_deep_clean else input('What should a person do to deep clean this? ')
        frequency_min: int = int(input('At a minimum, how often should this chore happen (in days)? '))
        frequency_max: int = int(input('At a maximum, how often should this chore happen (in days)? '))

        new_chore: Chore = Chore(name, key, description, (frequency_min, frequency_max), has_deep_clean, deep_clean)
        existing_chores.append(new_chore)

        user_wants_to_add: bool = input('Is there any more that you would like to add? (y/n) ').lower() == 'y'

    print('Okay will not add anymore chores.')
    print('Here are the chores now:')
    print_chores(existing_chores)

    return existing_chores


def add_housemates(housemates: typing.List[Housemate]) -> typing.List[Housemate]:
    pass


def main():
    chores: typing.List[Chore] = get_chores()
    chores = get_chores_from_user(chores)
    save_chores(chores)


if __name__ == '__main__':
    main()
