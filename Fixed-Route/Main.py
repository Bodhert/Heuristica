from Data import Data
from Vehicle import Vehicle
from Methods import *
import time
from matplotlib.cbook import tostr


def main():
    v = Vehicle()
    v2 = Vehicle()
    d = Data()
    d.saveRoute()
    
    #first method
    start = time.time()
    ConstructiveAlgorithm(d, v, 1, 30)
    end = time.time()
    print("elapsed time " + str( end - start))
    print()
    
    #second method
    start = time.time()
    NoiseAndConstruc(d, v2, 1, 30)
    end = time.time()
    print("elapsed time " + str( end - start))

    
if __name__ == "__main__": main()