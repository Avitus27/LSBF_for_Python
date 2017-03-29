import LSBF.py

def testFunc():
    myBloom = createBloomArray( 2, 2, 10, 0.5 )
    print("Should be False: " + str(checkInBloom(myBloom, 5)))
    addToBloom(myBloom, 5)
    print("Should be True: " + str(checkInBloom(myBloom, 5)))
    print("Should be True: " + str(checkInBloom(myBloom, 5.0000)))
    print("Should be True: " + str(localityBloomCheck(myBloom, 3.0000)))

