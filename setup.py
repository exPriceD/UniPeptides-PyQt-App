import os

def setupConfig():
    if not os.path.isdir("cfg"):
        os.mkdir("cfg")

    path = os.getcwd()

    #access_mode 'w' (for creating if not in dir)
    with open(f"{path}/cfg/Peptides.txt", 'w') as peptides:
        peptides.close()
    with open(f"{path}/cfg/User_config.txt", 'w') as config:
        config.close()
    with open(f"{path}/cfg/User_proteins.txt", "w") as user_proteins:
        user_proteins.close()
    with open(f"{path}/cfg/Log error.txt", "w") as logs:
        logs.close()
    with open(f"{path}/cfg/Database.txt", 'w') as database:
        database.close()
    with open(f"{path}/cfg/Proteins.txt", "w") as proteins:
        proteins.close()

    #access_mode 'r+' (for truncate)
    with open(f"{path}/cfg/Peptides.txt", 'r+') as peptides:
        peptides.truncate()
        peptides.close()
    with open(f"{path}/cfg/User_config.txt", 'r+') as config:
        config.truncate()
        config.close()
    with open(f"{path}/cfg/User_proteins.txt", "r+") as user_proteins:
        user_proteins.truncate()
        user_proteins.close()
    with open(f"{path}/cfg/Log error.txt", "r+") as logs:
        logs.truncate()
        logs.close()
    with open(f"{path}/cfg/Database.txt", 'r+') as database:
        database.truncate()
        database.close()
    with open(f"{path}/cfg/Proteins.txt", "r+") as proteins:
        proteins.truncate()
        proteins.close()
