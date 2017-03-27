import hashlib
import math

from bitarray import bitarray

def getArrayPos( input ):
	return ( int(bin(int(input, 16))[2:].zfill(8)[0:16], 2), int(bin(int(input, 16))[2:].zfill(8)[16:32], 2) )

def setArrayBit( outerArray, bitPosition ):
        return True

emptyArray = bitarray(2**16)
bloomArray = [None]

for count in xrange( 65536 ):
	bloomArray.append(emptyArray)


#hashlib.md5('a'.encode('utf-8'))
#hashlib.sha512('a')

#hashlib.md5('a'.encode('utf-8')).digest()

#print hashlib.sha512('a').hexdigest()

m5_a = hashlib.md5()

m5_a.update('a'.encode('utf-8'))

hex = m5_a.hexdigest()
binary = m5_a.digest()

#print(hex)
#print(hex[0:16])
#print(hex[16:32])


#print(len(binary))
#print(binary)
#print(binary[0:8])
#print(binary[8:16])

#print(len(bin(int(hex, 16))[2:].zfill(8)))

#print(bin(int(hex, 16)))
print("decimal here:")
print(int(bin(int(hex, 16))[2:].zfill(8)[0:16], 2))
print(int(bin(int(hex, 16))[2:].zfill(8)[16:32], 2))

print("test function:")
print(getArrayPos(hex))

myVar = getArrayPos(hex)

print(myVar[1])
