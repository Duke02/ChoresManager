import json
import typing

from chore_occurrence import ChoreOccurrence
from housemate import Housemate


def get_recipients(filepath: str = 'recipients.json') -> typing.List[Housemate]:
    print(f'Loading recipients from {filepath}.')

    recipients: typing.List[Housemate] = []
    with open(filepath, 'r') as f:
        recipients = [Housemate.from_json(recipient) for recipient in json.load(f)]
    print(f'Found {len(recipients)} recipients.')

    return recipients


def write_main_email_body(chore_history: typing.List[ChoreOccurrence]) -> str:
    lines: typing.List[str] = [f'Recent chore completions:']

    lines.extend([str(chore_occurrence) for chore_occurrence in chore_history])

    lines.append('\n')

    # TODO: Get all chores that should be done soon.

    return '\n'.join(lines)
