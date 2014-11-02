import re
import os
from BaseHandler import BaseHandler
##########################################################################


class GaussTargetHandler(BaseHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def findFiles(self, dir):
        files = [f for f in os.listdir(dir) if re.search('.\.png', f)]
        return files

    def collectResults(self, directory):
        files = self.findFiles(directory)
        if len(files) == 0:
            raise Exception("Could not locate files in the given directory")

        for f in files:
            fileName, fileExtension = os.path.splitext(f)
            self.saveFile(fileName, os.path.join(directory, f))
