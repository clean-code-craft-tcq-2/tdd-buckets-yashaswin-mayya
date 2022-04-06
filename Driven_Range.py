class driven_range:

    def main(self, inputData):
        inputData.sort()
        self.inputData = inputData.copy()
        return self.generateResult()

  
    def getRangeListInfo(self):
        cumulativeFrequency = 0
        rangeInfoList = []
        listCurrentPosition = 0
        while (cumulativeFrequency != len(self.inputData)):
            rangeOpenerElement = self.inputData[listCurrentPosition]
            rangeCloserPosition = self.getRangeCloserPosition(listCurrentPosition)
            frequency = rangeCloserPosition - listCurrentPosition + 1
            rangeCloserElement = self.inputData[rangeCloserPosition]
            rangeInfoList.append((rangeOpenerElement, rangeCloserElement, frequency))
            listCurrentPosition = rangeCloserPosition + 1
            cumulativeFrequency+=frequency
        return rangeInfoList


    def getRangeCloserPosition(self, listBeginPosition):
        rangeCloserPosition = listBeginPosition
        for i in range(listBeginPosition+1, len(self.inputData)):
            differenceInValues = (self.inputData[i]-self.inputData[rangeCloserPosition])
            if(differenceInValues==0 or differenceInValues==1):
                rangeCloserPosition = i
        return rangeCloserPosition
    
    def generateResult(self):
        self.printOnConsole('Range, Result')
        rangeInfoList = self.getRangeListInfo()
        rangeResult = {}
        for rangeInfo in rangeInfoList:
            rangeData = f'{rangeInfo[0]}-{rangeInfo[1]}'
            freqData = f'{rangeInfo[2]}'
            rangeResult.update({rangeData: freqData})
            self.printOnConsole(f'{rangeData}, {freqData}')
        self.printOnConsole('\n')
        return rangeResult
    
    def printOnConsole(self, rangeResult):
        print(rangeResult)
