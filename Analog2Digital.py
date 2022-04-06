ADC_12Bits = {'maxDigitalValue': 4094, 'scale': 10, 'offset': 0}
ADC_10Bits = {'maxDigitalValue': 1023, 'scale': 30, 'offset': 15}

class A2D:

    def convertAnalogToDigital(self, digitalValueRange, ADC_Sensor_Type):
        analogValueRange=[]
        for digitalValue in digitalValueRange:
            if (0<=digitalValue<=ADC_Sensor_Type['maxDigitalValue']):
                analogValue = abs(round((ADC_Sensor_Type['scale']*digitalValue/ADC_Sensor_Type['maxDigitalValue'])-ADC_Sensor_Type['offset']))
                analogValueRange.append(analogValue)
        return
