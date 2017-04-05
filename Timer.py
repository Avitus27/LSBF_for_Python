import LSBF
import random
import timeit
from time

current_milli_time = lambda: int(round(time.time() * 1000))

regularArray = []

def randomTest():
    myBloom = LSBF.LocalitySensitiveBloomFilter(2, 2, 5, 1)
    for i in xrange(100):
        x = random.randrange(0, 10000)
        myBloom.addToBloom(x)
        regularArray.insert(x)
        print(str(x))
    return myBloom

def iterativeCheck(array, testValue, localityRange):
    for x in array:
        if (x >= (testValue - localityRange)) and (x <= (testValue + localityRange)):
            return True
    return False

print("randomTest(): ")
myBloom = randomTest()
for i in xrange(10):
    inputFloat = float(raw_input("test a number for approximate presence: "))
    print("Timing LSBF:\r\n")
    a = current_milli_time()
    print(str(myBloom.localityBloomCheck(inputFloat)))
    b = current_milli_time()
    print("Took " + str(b-a) + "ms\r\n")

    print("Timing iterative approach:\r\n")
    a = current_milli_time()
    print(str(iterativeCheck(regularArray, inputFloat, 5)))
    b = current_milli_time()
    print("Took " + str(b-a) + "ms\r\n")
