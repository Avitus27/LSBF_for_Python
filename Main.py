import LSBF
import random

def testFunc():
    myBloom = LSBF.LocalitySensitiveBloomFilter( 2, 2, 10, 0.5 )
    print("Should be False: " + str(myBloom.checkInBloom(5)))
    myBloom.addToBloom(5)
    print("Should be True: " + str(myBloom.checkInBloom(5)))
    print("Should be True: " + str(myBloom.checkInBloom(5.000)))
    print("Should be True: " + str(myBloom.localityBloomCheck(3.0000, myBloom.LOCALITY_RANGE )))

def randomTest():
	myBloom = LSBF.LocalitySensitiveBloomFilter(2, 2, 5, 1)
	for i in xrange(100):
		x = random.randrange(0, 10000)
		myBloom.addToBloom(x)
		print(str(x))
	return myBloom

print("testFunc(): ")
testFunc()

print("randomTest(): ")
myBloom = randomTest()
for i in xrange(10):
	inputFloat = float(raw_input("test a number for approximate presence: "))
	if myBloom.localityBloomCheck(inputFloat, 5):
		print("Input was in or near a value in the bloom filter")
	else:
		print("Input was not near a value in the bloom filter")
