import hashlib
import math

from bitarray import bitarray

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
        self.floatString = "{0:." + str(floatPrecision) + "f}"
        emptyArray = bitarray(2**16)
        emptyArray.setall(False)
        self.bloomArray = []

        for count in range( 0, 65536 ):
            self.bloomArray.append(emptyArray)

    def setArrayBit( bloomArray, bitPosition ):
        bloomArray.bloomArray[bitPosition[0]][bitPosition[1]] = True
        return

    def getArrayPos( bloomArray, input ):
        #This takes the first 16 + 16 bits of the hash and turns it into a tuple, the position of a bit
        return ( int(bin(int(input, 16))[2:].zfill(8)[0:16], 2), int(bin(int(input, 16))[2:].zfill(8)[16:32], 2) )

    def addToBloom( bloomArray, input ):
        input = bloomArray.floatString.format(input)
        bloomArray.setArrayBit(bloomArray.getMD5HashPosition(input))
        if bloomArray.NUM_HASHES > 1:
            bloomArray.setArrayBit(bloomArray.getSHA1HashPosition(input))

    def checkInBloom( bloomArray, input ):
        input = bloomArray.floatString.format(input)
        if bloomArray.getMD5HashPresence( input ):
            #TODO What happens when there's only one hash
            return bloomArray.getSHA1HashPresence( input )
        return False

    def localityBloomCheck( bloomArray, input, range ):
        #TODO When there's only one hash
        if (range < bloomArray.LOCALITY_RESOLUTION):
            return bloomArray.checkInBloom( input )
        else:
            if not bloomArray.checkInBloom( input - range ):
                if not bloomArray.checkInBloom( input + range ):
                    if not bloomArray.localityBloomCheck( input, range - bloomArray.LOCALITY_RESOLUTION ):
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
