charsInBlock = 4
bitsInBlock = 8
numberOfBlocks = 4
 
# splits string into a list of 4 char blocks
def parseInput(userInput):
    length = (len(userInput) //charsInBlock)
    if len(userInput)%charsInBlock != 0:
        length +=1

    newarr = []
    for i in range(length):
        newarr.append(userInput[i*charsInBlock:(i*charsInBlock)+charsInBlock])
    return newarr

# converts char to its ascii value
def getAscii(userInput):
    asciiList = []
    for char in userInput:        
        asciiList.append(ord(char))
    return asciiList

# converts a decimal to binary
def DecimalToBinary(num):      
    binary = str(bin(num).replace("0b",""))
    if len(binary) != bitsInBlock:
        for i in range(bitsInBlock-len(binary)):
            binary = "0" + binary
    return binary

# calls DecimalToBinary and ensures the output is the correct size
def convertToBinary(asciiList):
    binaryList = []
    for asciiVal in asciiList:
        binary = DecimalToBinary(asciiVal)
        binaryList.insert(0,binary)

    for i in range(numberOfBlocks - len(binaryList)):
        binaryList.insert(0,"00000000")
    return binaryList

# converts binary to decimal
def binaryToDecimal(binary):       
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal     

# encodes the binary blocks
def encodeBlocks(binaryList):
    encodedList = []   
    encodedNum = '' 
    for block in range(charsInBlock):       
        for i in range(int(bitsInBlock/charsInBlock)):                  
            for j in range(numberOfBlocks):                
                encodedNum = (encodedNum +
                 binaryList[j][i+(int((bitsInBlock/charsInBlock))*block)])
    return int(encodedNum)

# manages the encoding process
def encode(userInput):
    finalResult = []
    parsedInput = parseInput(userInput)
    for inputSlice in parsedInput:
        asciiList = getAscii(inputSlice)
        binaryList = convertToBinary(asciiList)
        encodedNum = encodeBlocks(binaryList)
        result = binaryToDecimal(encodedNum)
        finalResult.append(result)        
    return finalResult

# splits a 32 bits into 8 bit blocks
def split(binaryList):
    arr = []
    for i in binaryList[::-1]:
        for j in range(numberOfBlocks):
            arr.append(i[j::numberOfBlocks])
    return arr

# manages the decoding process 
def decode(userInput):
    binaryList = [] 
    decodedString =""

    # convert decimals to binary   
    for i in range(len(userInput)):
        binaryList.append(DecimalToBinary(userInput[i]))

    # ensure binary is correct size
    for i in range(len(binaryList)): 
        while len(binaryList[i]) != bitsInBlock * numberOfBlocks:
            binaryList[i] = '0' + binaryList[i]      
    decodedList = split(binaryList)

    # convert list of char's to a string
    for i in decodedList:
        decodedString = chr(binaryToDecimal(int(i))) + decodedString
    decodedString = decodedString.replace("\x00","")
    return decodedString
    
