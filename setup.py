import json

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

