import re
import os
import os.path

from BaseHandler import BaseHandler
###############################################################################
FILE_WITH_NUMBERS = "radLenghtOut.txt"
PLOTS_DIRECTORY = "plots"
FIELD_NAME = 0
FIELD_CENTRAL_VALUE = 1
FIELD_STATERR_VALUE = 2
###############################################################################


class GaussRadLengthHandler(BaseHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def findFiles(self, dir):
        result = []
        for root, subFolders, files in os.walk(dir):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext == '.png':
                    result.append(os.path.join(root, file))
        
        return result

    def collectNumbers(self, directory):
        file_with_numbers = open(os.path.join(directory, FILE_WITH_NUMBERS))
        
        is_header = True
        for line in file_with_numbers:
            if is_header:
                is_header = False
                continue

            fields = line.split('&')
            self.saveFloat(
                name=fields[FIELD_NAME].strip(),
                data=float(fields[FIELD_CENTRAL_VALUE].split(r"\pm")[0]),
                group="Gauss Radiation Length"
            )

    def collectResults(self, directory):
        # Save files
        self.collectNumbers(directory)

        files = self.findFiles(os.path.join(directory, PLOTS_DIRECTORY))
        if len(files) == 0:
            raise Exception("Could not locate files in the given directory")

        for f in files:
            fileName, fileExtension = os.path.splitext(f)
            self.saveFile(os.path.basename(fileName), f)

