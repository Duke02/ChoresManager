import typing


class Chore:

    def __init__(self, name: str, key: str, description: str, frequency: typing.Tuple[int, int], has_deep_clean: bool,
                 deep_clean: typing.Optional[str] = None):
        self.name = name.strip()
        self.key = key.strip()
        self.description = description.strip()
        self.frequency_max = max(frequency)
        self.frequency_min = min(frequency)
        self.has_deep_clean = has_deep_clean
        self.deep_clean = deep_clean.strip() if has_deep_clean else ''

    @staticmethod
    def from_json(json_obj: typing.Dict):
        name: str = json_obj["name"].strip()
        key: str = json_obj["key"].strip()
        description: str = json_obj["description"].strip()
        frequency_min: int = json_obj["frequency_min"]
        frequency_max: int = json_obj["frequency_max"]
        has_deep_clean: bool = json_obj["has_deep_clean"]
        deep_clean: str = json_obj["deep_clean"].strip() if has_deep_clean else ''
        return Chore(name, key, description, (frequency_min, frequency_max), has_deep_clean, deep_clean)
