from Data import Data
from Vehicle import Vehicle
from Methods import *
import time
from matplotlib.cbook import tostr


def main():
    vehicle = Vehicle()
    data = Data()
    data.saveRoute()
    
    EvolutiveAlgorithm(data,vehicle)
    
    
    
if __name__ == "__main__": main()