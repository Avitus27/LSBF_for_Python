import LSBF

def testFunc():
    myBloom = LSBF.LocalitySensitiveBloomFilter( 2, 2, 10, 0.5 )
    print("Should be False: " + str(myBloom.checkInBloom(5)))
    myBloom.addToBloom(5)
    print("Should be True: " + str(myBloom.checkInBloom(5)))
    print("Should be True: " + str(myBloom.checkInBloom(5.000)))
    print("Should be True: " + str(myBloom.localityBloomCheck(3.0000, myBloom.LOCALITY_RANGE )))

testFunc()

