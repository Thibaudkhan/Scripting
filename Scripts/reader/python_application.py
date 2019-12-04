# Dans un repertoire
# Detecter les fichers .txt .json et .yaml
# L'application doit detecter quand il y a une modification dans les fichier
# L'application doit copier les fichiers qui ont étaient modifier
# Créer une log des modifications et l'afficher

# Les signature (SHA256)

import argparse
from os import listdir, walk, path
from os.path import getctime, getsize, getatime, getmtime
import time


def detection_file():
    """
    :return:
    """

    def update_CONFIG(value_of_file):
        """
        :param value_of_file:
        :return:
        """
        CONFIG["directory"] = value_of_file[0].split(":")[1]
        CONFIG["timer"] = value_of_file[1].split(":")[1]

    # ====

    CONFIG = {}

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args().file.readlines()

    if ".json" in str(parser.parse_args()):
        update_CONFIG(("".join(args).replace('"', '').replace(' /', '/').replace('\n', '').replace("}", "")).split(","))
    elif ".txt" in str(parser.parse_args()):
        update_CONFIG(("-//-".join(args).replace('"', '').replace('\n', '').replace(' /', '/')).split("-//-"))
    elif ".yaml" in str(parser.parse_args()):
        update_CONFIG(("-//-".join(args).replace('"', '').replace('\n', '').replace(' /', '/')).split("-//-"))
    else:
        print("ERROR type of file not found")

    return CONFIG


def listing_file(CONFIG):
    """
    :param CONFIG:
    :return:
    """

    fileList = []
    RESULT = {}

    for (directory, underDirectories, files) in walk(CONFIG["directory"]):
        fileList.extend(files)
        for i in files:
            RESULT[i] = {
                "directory": directory,
                "last_change_metadata": getctime(directory + '/' + i),
                "file_size": getsize(directory + '/' + i),
                "last_access": getatime(directory + '/' + i),
                "last_change": getmtime(directory + '/' + i)
            }

    # getaTime(i)
    # getmTime(i)

    return RESULT


def main():
    """
    :return:
    """

    print(" ")
    print("=================================================")
    print("           ---------------------------           ")
    print("                      Exo 2                      ")
    print("           ---------------------------           ")
    print("=================================================")
    print(" ")

    CONFIG = detection_file()
    INFO_FILELIST = {}

    i = 0
    while i <= int(CONFIG["timer"]):
        INFO_FILELIST[time.asctime()] = listing_file(CONFIG)
        time.sleep(2)
        i += 1

    #    PRINTS    #
    for i, j in CONFIG.items():
        print("CONFIG =>", i, "=", j)

    for i, j in INFO_FILELIST.items():
        print(" ")
        print("fileList => ", i)
        for k, l in j.items():
            print(" ")
            print("    ", k)
            for m, n in l.items():
                print("        ", m, " : ", n)
    # // PRINTS // #

    print(" ")


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()