import re
import os
import os.path

from BaseHandler import BaseHandler
###############################################################################
FILE_WITH_NUMBERS = "radLenghtOut.txt"
FIELD_NAME = 0
FIELD_CENTRAL_VALUE = 2
FIELD_STATERR_VALUE = 4
###############################################################################


class GaussRadLengthHandler(BaseHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def findFiles(self, dir):
        files = [f for f in os.listdir(dir) if re.search('.\.png', f)]
        return files

    def collectNumbers(self, directory):
        file_with_numbers = open(os.path.join(directory, FILE_WITH_NUMBERS))
        for line in file_with_numbers:
            fields = line.split()
            self.saveFloat(
                name=fields[FIELD_NAME],
                value=float(fields[FIELD_CENTRAL_VALUE]),
                group="Gauss Radiation Length"
            )

    def collectResults(self, directory):
        # Save files
        files = self.findFiles(directory)
        if len(files) == 0:
            raise Exception("Could not locate files in the given directory")

        for f in files:
            fileName, fileExtension = os.path.splitext(f)
            self.saveFile(fileName, os.path.join(directory, f))
