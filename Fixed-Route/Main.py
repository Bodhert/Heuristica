from Data import Data
from Vehicle import Vehicle
from Methods import *


def main():
    v = Vehicle()
    d = Data()
    d.saveRoute()
#     d.generateNoise()
    ConstructiveAlgorithm(d, v, 1, 10)
#     d.printDataFromFile()
    print("test")
    
if __name__ == "__main__": main()