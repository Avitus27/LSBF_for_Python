import LSBF

def testFunc():
    myBloom = LSBF.LocalitySensitiveBloomFilter( 2, 2, 10, 0.5 )
    print("Should be False: " + str(myBloom.checkInBloom(5)))
    addToBloom(myBloom, 5)
    print("Should be True: " + str(checkInBloom(myBloom, 5)))
    print("Should be True: " + str(checkInBloom(myBloom, 5.0000)))
    print("Should be True: " + str(localityBloomCheck(myBloom, 3.0000)))

testFunc()

