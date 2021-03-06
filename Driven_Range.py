
class driven_range:

    def main(self, inputData):
        inputData.sort()
        self.inputData = inputData.copy()
        return self.generateResult()
    
    def convertDigitalToAnalog(self, digitalValueRange, ADC_Sensor_Type):
        # Formula used to convert Digital to Analog:
        # 
        # Analog_Value = ((Scale * Digital_Value) / Max._Digital_Value_permissible) - Offset
        # 
        # For 12 Bit:
        #   Scale = 10                              [10A - 0A = 10]
        #   Max._Digital_Value_permissible = 4094
        #   Offset = 0                              [As no Negative reading is applicable]
        # 
        # For 10 Bit:
        #   Scale = 30                              [15A - (-15A) = 30]
        #   Max._Digital_Value_permissible = 1023
        #   Offset = 15                              [As negative values upto -15 are applivale]
        # 
        analogValueRange=[]
        maxDigitalValue, scale, offset = self.sensorParameters(ADC_Sensor_Type)
        for digitalValue in digitalValueRange:
            if (0<=digitalValue and digitalValue<=maxDigitalValue):
                analogValue = abs(round((scale*digitalValue/maxDigitalValue)-offset))
                analogValueRange.append(analogValue)
        return analogValueRange
    
    def sensorParameters(self, ADC_Sensor_Type):
        if (ADC_Sensor_Type == '12Bits'):
            maxDigitalValue = 4094
            scale = 10
            offset = 0
        else:
            maxDigitalValue = 1023
            scale = 30
            offset = 15
        return maxDigitalValue, scale, offset


  
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
