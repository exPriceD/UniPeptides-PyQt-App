import json

#["P04439", "O95905", "P42694", "P08246", "Q6ZWK4", "P01889"]
def creatingLogs():
    logs = {
        "missing": {
            "proteins": []
        },
        "siteProblems": False,
        "unexpectedError": False
    }

    with open("errorLogs.json", "w") as errorLogs:
        json.dump(logs, errorLogs, indent=4)


def setupConfig():
    config = {
        "proteins": {
            "value": []
        },
        "peptides": {
            "value": []
        },
        "savePath": {
            "value": ''
        },
        "databasePath": {
            "value": ''
        },
        "proteinsPath": {
            "value": ''
        },
        "excelFilters": {
            "entryIdentifier": False,
            "entryName": False,
            "entryType": False,
            "fullName": False,
            "scientificName": False,
            "commonName": False,
            "genes": False,
            "proteinExistence": False,
            "length": False,
            "massDa": False,
            "category": False,
            "id": False,
            "sequence": False,
            "sequence_length": False,
            "occurrence": False,
            "relative": False,
            "position": False,
            "nter": False,
            "cter": False
        }
    }

    with open("config.json", "w") as json_cfg:
        json.dump(config, json_cfg, indent=4)


def saveFilters():
    with open("config.json", "r") as json_cfg:
        config_data = json.load(json_cfg)
        config_data["proteins"]["value"] = []
        config_data["peptides"]["value"] = []
        config_data["savePath"]["value"] = ''
        config_data["databasePath"]["value"] = ''
        config_data["proteinsPath"]["value"] = ''
    with open("config.json", "w") as json_cfg:
        json.dump(config_data, json_cfg, indent=4)
