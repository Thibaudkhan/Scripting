import argparse


class Params:

    def detection_file(self):
        """
        detect a config file
        if a config file => stock in dict "CONFIG" a value
        """

        def update_CONFIG(value_of_file):
            """
            add to config file
            """
            CONFIG["value"] = value_of_file[0].split(":")[1]
            CONFIG["method"] = value_of_file[1].split(":")[1]

        # ====

        CONFIG = {}

        parser = argparse.ArgumentParser()
        parser.add_argument('file', type=argparse.FileType('r'))
        args = parser.parse_args().file.readlines()

        if ".txt" in str(parser.parse_args()):
            update_CONFIG(("-//-".join(args).replace('"', '').replace('\n', '').replace(' /', '/')).split("-//-"))
        else:
            print("ERROR type of file not found")

        return CONFIG