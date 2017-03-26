from pybloom import BloomFilter

bf = BloomFilter(capacity=10000, error_rate=0.0001)

[bf.add(x) for x in range(10)]


