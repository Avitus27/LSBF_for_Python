import hashlib
import math

from bitarray import bitarray

#Pseudo-constants
FLOAT_PRECISION = 0
NUM_HASHES = 0
LOCALITY_RANGE = 0
LOCALITY_RESOLUTION = 0

floatString = "{0:." + str(FLOAT_PRECISION) + "f}"

class LocalitySensitiveBloomFilter:

    #Bloom Filter Basic Operations
    def __init__( self, floatPrecision, hashes, bloomRange, resolution ):
        if not floatPrecision >= 0:
            return None # floatPrecision needs to be positive
        self.FLOAT_PRECISION = floatPrecision
        if not hashes > 0:
            return None # We need at lest 1 hashing algorithm, upper limit is TODO
        self.NUM_HASHES = hashes
        self.LOCALITY_RANGE = bloomRange
        self.LOCALITY_RESOLUTION = resolution
        emptyArray = bitarray(2**16)
        emptyArray.setall(False)
        self.bloomArray = []

        for count in range( 0, 65536 ):
            self.bloomArray.append(emptyArray)

    #def createBloomArray( floatPrecision, hashes, bloomRange, resolution ):
    #    if not floatPrecision >= 0:
    #        return None # floatPrecision needs to be positive
    #    FLOAT_PRECISION = floatPrecision
    #    if not hashes > 0:
    #        return None # We need at lest 1 hashing algorithm, upper limit is TODO
    #    NUM_HASHES = hashes
    #    LOCALITY_RANGE = bloomRange
    #    LOCALITY_RESOLUTION = resolution
    #    emptyArray = bitarray(2**16)
    #    emptyArray.setall(False)
    #    bloomArray = []

    #    for count in range( 0, 65536 ):
    #        bloomArray.append(emptyArray)

    #    return bloomArray

    def setArrayBit( bloomArray, bitPosition ):
        bloomArray.bloomArray[bitPosition[0]][bitPosition[1]] = True
        return

    def getArrayPos( bloomArray, input ):
        #This takes the first 16 + 16 bits of the hash and turns it into a tuple, the position of a bit
        return ( int(bin(int(input, 16))[2:].zfill(8)[0:16], 2), int(bin(int(input, 16))[2:].zfill(8)[16:32], 2) )

    def addToBloom( bloomArray, input ):
        input = floatString.format(input)
        bloomArray.setArrayBit(bloomArray.getMD5HashPosition(input))
        if NUM_HASHES > 1:
            bloomArray.setArrayBit(bloomArray.getSHA1HashPosition(input))


    def checkInBloom( bloomArray, input ):
        input = floatString.format(input)
        if bloomArray.getMD5HashPresence( input ):
            #TODO What happens when there's only one hash
            return bloomArray.getSHA1HashPresence( input )
        return False

    def localityBloomCheck( bloomArray, input, range ):
        #TODO When there's only one hash
        if (range < bloomArray.LOCALITY_RESOLUTION) or (bloomArray.LOCALITY_RESOLUTION == 0):
            return bloomArray.checkInBloom( input )
        else:
            if not bloomArray.checkInBloom( input - bloomArray.LOCALITY_RANGE ):
                if not bloomArray.checkInBloom( input + bloomArray.LOCALITY_RANGE ):
                    if not bloomArray.localityBloomCheck( input, bloomArray.LOCALITY_RANGE - bloomArray.LOCALITY_RESOLUTION ):
                        return False
            return True

    #Hash Functions
    #MD5 Based
    def getMD5HashPosition( bloomArray, input ):
        m5 = hashlib.md5()
        m5.update(str(input).encode('utf-8'))
        return bloomArray.getArrayPos(m5.hexdigest())

    def getMD5HashPresence( bloomArray, input ):
        inputPosition = bloomArray.getMD5HashPosition( input )
        return bloomArray.bloomArray[inputPosition[0]][inputPosition[1]]

    #SHA1 Based
    def getSHA1HashPosition( bloomArray, input ):
        sha1 = hashlib.sha1()
        sha1.update(str(input).encode('utf-8'))
        return bloomArray.getArrayPos(sha1.hexdigest())

    def getSHA1HashPresence( bloomArray, input ):
        inputPosition = bloomArray.getSHA1HashPosition( input )
        return bloomArray.bloomArray[inputPosition[0]][inputPosition[1]]

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
