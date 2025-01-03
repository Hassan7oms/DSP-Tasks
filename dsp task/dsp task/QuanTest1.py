def QuantizationTest1(Your_EncodedValues,Your_QuantizedValues):
    expectedEncodedValues=[]
    expectedQuantizedValues=[]
    file_name="C:\\Users\\bacily\\Desktop\\DSP\\dsp task\\GUI\\Task\\Task\\Quan1_Out.txt"
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V2=str(L[0])
                V3=float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    print(f"Expected Encoded Values Length: {len(expectedEncodedValues)}")
    print(f"Expected Quantized Values Length: {len(expectedQuantizedValues)}")
    print(f"Your Encoded Values Length: {len(Your_EncodedValues)}")
    print(f"Your Quantized Values Length: {len(Your_QuantizedValues)}")
    if( (len(Your_EncodedValues)!=len(expectedEncodedValues)) or (len(Your_QuantizedValues)!=len(expectedQuantizedValues))):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_EncodedValues)):
        if(Your_EncodedValues[i]!=expectedEncodedValues[i]):
            print(f"Mismatch at index {i}: Expected {expectedEncodedValues}, but got {Your_EncodedValues}")
            print("QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one") 
            return
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print("QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one") 
            return
    print("QuantizationTest1 Test case passed successfully")