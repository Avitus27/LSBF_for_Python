import hashlib
import math

from bitarray import bitarray

def getArrayPos( input ):
    return ( int(bin(int(input, 16))[2:].zfill(8)[0:16], 2), int(bin(int(input, 16))[2:].zfill(8)[16:32], 2) )

def setArrayBit( bloomArray, bitPosition ):
    bloomArray[bitPosition[0]][bitPosition[1]] = True
    return

def createBloomArray():
    emptyArray = bitarray(2**16)
    emptyArray.setall(False)
    bloomArray = []

    for count in range( 0, 65536 ):
        bloomArray.append(emptyArray)

    return bloomArray

def getMD5HashPosition( input ):
    m5_a = hashlib.md5()
    m5_a.update(input.encode('utf-8'))
    return getArrayPos(m5_a.hexdigest())

def getMD5HashPresence( bloomArray, input ):
    inputPosition = getMD5HashPosition( input )
    return bloomArray[inputPosition[0]][inputPosition[1]]

#hashlib.md5('a'.encode('utf-8'))
#hashlib.sha512('a')

#hashlib.md5('a'.encode('utf-8')).digest()

#print hashlib.sha512('a').hexdigest()

#print(hex)
#print(hex[0:16])
#print(hex[16:32])


#print(len(binary))
#print(binary)
#print(binary[0:8])
#print(binary[8:16])

#print(len(bin(int(hex, 16))[2:].zfill(8)))

#print(bin(int(hex, 16)))
#print("decimal here:")
#print(int(bin(int(hex, 16))[2:].zfill(8)[0:16], 2))
#print(int(bin(int(hex, 16))[2:].zfill(8)[16:32], 2))
#
#print("test function:")
#print(getArrayPos(hex))
#
#myVar = getArrayPos(hex)
#
#print(myVar[1])
