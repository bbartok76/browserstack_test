from pathlib import Path
import json
import yaml


def get_credentials():
    # if Path("credentials.yaml").is_file():
    #     with open("credentials.yaml", encoding="utf-8") as file:
    #         return yaml.load(file, Loader=yaml.FullLoader)
    if Path("credentials.json").is_file():
        with open("credentials.json", encoding="utf-8") as file:
            return json.load(file)
