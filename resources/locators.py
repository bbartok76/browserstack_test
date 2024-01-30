import yaml


def get_locators(filename: str = "./resources/locators.yaml") -> dict:
    with open(filename, encoding="utf-8") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


locators = get_locators()
