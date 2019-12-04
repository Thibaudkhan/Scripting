# Dans un repertoire
# Detecter les fichers .txt .json et .yaml
# L'application doit detecter quand il y a une modification dans les fichier
# L'application doit copier les fichiers qui ont été modifié
# Créer une log des modifications et l'afficher

# Les signature (SHA256)

import argparse
import shutil
from os import listdir, walk, path, makedirs
from os.path import getctime, getsize, getatime, getmtime, exists
import time


def read_in_consolelog_file(message):
    file = open("Backup/console_log.txt", "a")
    file.write("\n")
    file.write(message)
    file.close()


def backup_of_modified_files(NEW_BACKUP, OLD_BACKUP, timing):

    new_val = []

    if not exists(timing.replace(" ", "_")):
        makedirs("Backup/" + timing.replace(" ", "_"))

    if NEW_BACKUP.keys() == OLD_BACKUP.keys():
        for keys, values in OLD_BACKUP.items():
            if values != NEW_BACKUP[keys]:
                new_val.append(keys)
                shutil.copy(NEW_BACKUP[keys]["directory"] + "/" + keys,
                    "Backup/"
                    + timing.replace(" ", "_") + "/" + keys)

    return new_val


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
    print("Press CTRL + C to quit")
    print(" ")

    CONFIG = detection_file()
    INFO_FILELIST = {}

    while True:
        if len(INFO_FILELIST.keys()) == 0:
            INFO_FILELIST[time.asctime()] = listing_file(CONFIG)
        elif listing_file(CONFIG) != INFO_FILELIST[str(max(INFO_FILELIST.keys()))]:
            modify_files = backup_of_modified_files(listing_file(CONFIG), INFO_FILELIST[str(max(INFO_FILELIST.keys()))], time.asctime())
            print(modify_files)
            read_in_consolelog_file(time.asctime() + "  =>  modify files  =>  " + " ".join(modify_files))
            INFO_FILELIST[time.asctime()] = listing_file(CONFIG)

        time.sleep(int(CONFIG["timer"]))

    '''
    # == PRINTS == #
    for i, j in CONFIG.items():
        print("CONFIG =>", i, "=", j)

    print(" ")

    for i, j in INFO_FILELIST.items():
        print(" ")
        print("fileList => ", i)
        for k, l in j.items():
            print(" ")
            print("    ", k)
            for m, n in l.items():
                print("        ", m, " : ", n)
    # // PRINTS // #
    '''
    print(" ")


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()