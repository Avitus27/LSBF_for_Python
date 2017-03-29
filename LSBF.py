import hashlib
import math

from bitarray import bitarray

FLOAT_PRECISION = 0
NUM_HASHES = 0
LOCALITY_RANGE = 0
LOCALITY_RESOLUTION = 0

floatString = "{0:." + str(FLOAT_PRECISION) + "f}"

def getArrayPos( input ):
    return ( int(bin(int(input, 16))[2:].zfill(8)[0:16], 2), int(bin(int(input, 16))[2:].zfill(8)[16:32], 2) )

def setArrayBit( bloomArray, bitPosition ):
    bloomArray[bitPosition[0]][bitPosition[1]] = True
    return

def createBloomArray( floatPrecision, hashes, bloomRange, resolution ):
    FLOAT_PRECISION = floatPrecision
    NUM_HASHES = hashes
    LOCALITY_RANGE = bloomRange
    LOCALITY_RESOLUTION = resolution
    emptyArray = bitarray(2**16)
    emptyArray.setall(False)
    bloomArray = []

    for count in range( 0, 65536 ):
        bloomArray.append(emptyArray)

    return bloomArray

def getMD5HashPosition( input ):
    m5 = hashlib.md5()
    m5.update(str(input).encode('utf-8'))
    return getArrayPos(m5.hexdigest())

def getMD5HashPresence( bloomArray, input ):
    inputPosition = getMD5HashPosition( input )
    return bloomArray[inputPosition[0]][inputPosition[1]]

def getSHA1HashPosition( input ):
    sha1 = hashlib.sha1()
    sha1.update(str(input).encode('utf-8'))
    return getArrayPos(sha1.hexdigest())

def getSHA1HashPresence( bloomArray, input ):
    inputPosition = getSHA1HashPosition( input )
    return bloomArray[inputPosition[0]][inputPosition[1]]


def addToBloom( bloomArray, input ):
    input = floatString.format(input)
    setArrayBit(bloomArray, getMD5HashPosition(input))
    setArrayBit(bloomArray, getSHA1HashPosition(input))

def checkInBloom( bloomArray, input ):
    input = floatString.format(input)
    if getMD5HashPresence( bloomArray, input ):
        return getSHA1HashPresence( bloomArray, input )
    return False

def localityBloomCheck( bloomArray, input, range, resolution ):
    if range < resolution:
        return checkInBloom( bloomArray, input )
    else:
        if not checkInBloom( bloomArray, input - range):
            if not checkInBloom( bloomArray, input + range):
                if not localityBloomCheck( bloomArray, input, range - resolution, resolution ):
                    return False
        return True

def testFunc():
    myBloom = createBloomArray( 2, 2, 10, 0.5 )
    print("Should be False: " + str(checkInBloom(myBloom, 5)))
    addToBloom(myBloom, 5)
    print("Should be True: " + str(checkInBloom(myBloom, 5)))
    print("Should be True: " + str(checkInBloom(myBloom, 5.0000)))
