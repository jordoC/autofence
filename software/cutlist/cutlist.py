#!/usr/bin/python

import csv

#######################################################################
class CutList():
    ###################################################################
    def __init__(self,filename):
        self._csvFile = self._openFile(filename)
        self._reader = csv.DictReader(self._csvFile)
        self.cutlist = []
        self._readFile()
        self._debugFileOut()
        self._closeFile()
    ###################################################################
    def _openFile(self,filename):
        csvFile = open(filename, 'rb')
        return csvFile
    ###################################################################
    def _closeFile(self):
        self._csvFile.close()
    ###################################################################
    def _readFile(self):
        for row in self._reader:
            self.cutlist.append(row)
        #print self.cutlist
    ###################################################################
    def _debugFileOut(self):
        for row in self._reader:
            print row
#######################################################################
if __name__ == "__main__":
    cutlist = CutList(filename='test.clf')
