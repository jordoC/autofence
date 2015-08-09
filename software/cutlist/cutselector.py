#!/usr/bin/python

from cutlist import CutList

#######################################################################
class CutSelector():
    ###################################################################
    def __init__(self, filename):
        self._cutlist = CutList(filename)
        self._proposedPiece = {}
    ###################################################################
    def determineLength(self, defectLen):
        '''
        Desc:   Parses the cutlist for the best piece to cut, then returns
                the proposed cut value for verification
        '''
        self._proposedPiece = self._cutlist.seekPiece(defectLen)
        proposedCutLen = self._proposedPiece['Length as Cut']
        return proposedCutLen
    ###################################################################
    def moveFence(self, cutLen):
        '''
        Desc:   Parses the cutlist for the best piece to cut, then returns
                the proposed cut value for verification
        '''
        #TODO:  Need to implement this depending on the motor/HW selected
        #       Will most likely take the form of some sort of modbus commands
        return
    ###################################################################
    def verifyCut(self, isVerified):
        '''
        Desc:   Removes the proposed piece from the cutlist if isVerified
                is True
        '''
        buildLen = self._proposedPiece['Length as Built']
        cutLen = self._proposedPiece['Length as Cut']
        if (isVerified is True):
            self._cutlist.delPiece(buildLen=buildLen, cutLen=cutLen)

#######################################################################
if __name__ == "__main__":
    cutsel = CutSelector('test.clf')
    propLen = cutsel.determineLength(defectLen=21)
    print 'Proposed Length', propLen
    cutsel.verifyCut(True)
