import argparse
import json
# Dans un repertoire
# Detecter les fichers .txt .json et .yaml
# L'application doit detecter quand il y a une modification dans les fichier
# L'application doit copier les fichiers qui ont étaient modifier
# Créer une log des modifications et l'afficher

# Les signature (SHA256)


def detection_file():

    def update_CONFIG(value_of_file):
        CONFIG["directory"] = value_of_file[0].split(":")[1]
        CONFIG["timer"] = value_of_file[1].split(":")[1]

    # ====

    CONFIG = {}

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args().file.readlines()

    if ".json" in str(parser.parse_args()):
        update_CONFIG(("".join(args).replace('"', '').replace('\n', '').replace(' ', '').replace("}", "")).split(","))
    elif ".txt" in str(parser.parse_args()):
        update_CONFIG(("-//-".join(args).replace('"', '').replace('\n', '').replace(' ', '')).split("-//-"))
    elif ".yaml" in str(parser.parse_args()):
        update_CONFIG(("-//-".join(args).replace('"', '').replace('\n', '').replace(' ', '')).split("-//-"))
    else:
        print("ERROR type of file not found")

    return CONFIG


def main():
    print(" ")
    print("=================================================")
    print("           ---------------------------           ")
    print("                      Exo 2                      ")
    print("           ---------------------------           ")
    print("=================================================")
    print(" ")

    CONFIG = detection_file()

    for i, j in CONFIG.items():
        print(i, "=>", j)


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()