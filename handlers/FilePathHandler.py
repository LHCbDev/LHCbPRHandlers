import os, sys, re
from BaseHandler import BaseHandler
from xml.etree.ElementTree import ElementTree
from xml.parsers.expat import ExpatError

class FilePathHandler(BaseHandler):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.finished = False
        self.results = []

    def collectResults(self,directory):
        logfile = 'run.log'
        run_path = os.path.join(directory, logfile)

        regxp = ".*(/afs/cern.ch/lhcb/software/profiling/releases/[A-Z0-9]+/\w+_[\d\w]+/[\d\w\-]+/[\d_]+[\w\d]+/.*)'"
        path_line = ""
        try:
           loglines = open(run_path, 'r')
           for l in loglines.readlines():
              m = re.match(regxp, l)
              if m != None:
                 path_line = m.group(1)
                 break
           print 'Path ', path_line, ' added.'
           loglines.close()
        except IOError:
           raise Exception(str(self.__class__)+": File not found, this handler expects 'run.log' file in the result directory")
         
        if os.path.exists(run_path) :
           self.saveString("Path", path_line, "Results", "JobInfo")
           print 'Path ', path_line, ' added.'
        else:
           print 'File or path does not exist (file: ' + run_path + ')'

if __name__ == "__main__":
    fh = FilePathHandler()
    fh.collectResults('./')
