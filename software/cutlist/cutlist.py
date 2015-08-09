#!/usr/bin/python
import csv

#######################################################################
class CutList():
    ###################################################################
    def __init__(self,filename):
        self._csvFile = self._openFile(filename)
        self._reader = csv.DictReader(self._csvFile)
        self._cutlist = []
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
            self._cutlist.append(row)
        #print self._cutlist
    ###################################################################
    def _debugFileOut(self):
        '''For debug purposes only'''
        for row in self._reader:
            print row
    ###################################################################
    def delPiece(self,buildLen,cutLen):
        '''
        Desc:   Search trough the cutlist to find a piece of the given 
                cut length and build length, delete the piece from the cutlist,
                and return the piece (entry) from the cutlist that was deleted.
                If the piece does not exist in the cutlist, then return None
        '''
        #print 'CUTLIST',self._cutlist
        for piece in self._cutlist:
            pieceBuildLen = piece['Length as Built']
            pieceCutLen = piece['Length as Cut']
            if ((pieceBuildLen == buildLen)and(pieceCutLen == cutLen)):
                pieceToDel = piece
                self._cutlist.remove(piece)
                #print 'CUTLIST',self._cutlist
                return pieceToDel
        return None
    ###################################################################
    def peekPiece(self,buildLen,cutLen):
        '''
        Desc:   Check (peek) to see a piece of a specific build/cut length
                exists in the cutlist. Return True if it does, False 
                otherwise.
        '''
        buildLen = float(buildLen) 
        cutLen = float(cutLen) 
        for piece in self._cutlist:
            pieceBuildLen = float(piece['Length as Built'])
            pieceCutLen = float(piece['Length as Cut'])
            if ((pieceBuildLen == buildLen)and(pieceCutLen == cutLen)):
                return True
        return False
    ###################################################################
    def seekPiece(self,defectLen):
        '''
        Desc:   Hunt through the cutlist for the piece closest to the
				specified defect length. Return the piece from the list
				that is the closest while still being shorter than
				the specified defect length.
        '''
        defectLen = float(defectLen)
        #Just a big number to make sure that we start from a reasonable spot
        #NOTE:This constant should be large enough even in metric (65m), but
        #		if things go terribly, terribly, sadly awry then this would be
        #		a good spot to start debugging (it's a bit hacky)
        deltaBest = 65535
        pieceBest = None
        for piece in self._cutlist:
            pieceCutLen = float(piece['Length as Cut'])
            delta = defectLen - pieceCutLen
            #print delta
            if ((delta >= 0) and (delta < deltaBest)):
                deltaBest = delta
                pieceBest = piece
        return pieceBest

#######################################################################
if __name__ == "__main__":
    cutlist = CutList(filename='test.clf')
    delPc = cutlist.delPiece(buildLen=31.25, cutLen=25.25)
    print delPc
    print'PEEK:',cutlist.peekPiece(buildLen=30.25, cutLen=25.25)
    delPc = cutlist.delPiece(buildLen=30.25, cutLen=25.25)
    print'PEEK:',cutlist.peekPiece(buildLen=30.25, cutLen=25.25)
    print delPc
    bestPc = cutlist.seekPiece(40.375)
    print bestPc
