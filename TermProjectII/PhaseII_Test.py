#########################################
##  Do not change this file            ##
## Your codes must work with this file ##
#########################################

import math
import random
import string
import warnings
import pyprimes
import DS       # This is the file from Phase I
import Tx       # This is the first file you have to submit in the second phase 
import PoW      # This is the second file you have to submit in the second phase 
import os.path
import hashlib
import sys

if sys.version_info < (3, 6):
    import sha3

def random_string(size=6, chars=string.ascii_uppercase + string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def ReadPubParams(filename):
    if os.path.isfile(filename):
        f = open(filename, "r")
        q = int(f.readline())
        p = int(f.readline())
        g = int(f.readline())
        f.close()
        return q, p, g
    else:
        return -1

def checkDSparams(q, p, g):
    warnings.simplefilter('ignore')
    check = pyprimes.isprime(q)
    warnings.simplefilter('default')
    if check == False:
        return -1
    
    warnings.simplefilter('ignore')
    check = pyprimes.isprime(p)
    warnings.simplefilter('default')
    if check == False:
        return -2
   
    r = (p-1)%q
    if(r != 0):
        return -3

    k = (p-1)//q

    x = pow(g, k, p)
    if (x==1):
        return -4
    y = pow(g,q,p)
    if (y!=1):
        return -4

    return 0

def CheckBlock(filename, q, p, g):
    if os.path.isfile(filename):
        f = open(filename, "r")
        block = f.readlines()
        if len(block)%6 != 0:
            print("Incorrect file format")
            return -10000
        block_count = len(block)//6
        for i in range(0, block_count):
            pk = int(block[i*6+2][24:])
            s = int(block[i*6+4][15:])
            h = int(block[i*6+5][15:])
            tx = "".join(block[i*6: i*6+4])
            ver = DS.SignVer(tx.encode('UTF-8'), s, h, q, p, g, pk)
            if ver == -1:
                return -i
        return 0
    else:
        print("File does not exist")
        return -10000

##############        
# Student Part
# Test your public parameters with this routine
(q, p, g) = ReadPubParams("pubparams.txt")
# uncomment the next line if you want to check the public parameters
#print(checkDSparams(q, p, g)) 

# This is for generating random transactions
# You should have a function with the name "Tx.gen_random_tx()" in "Tx.py"
tx_blk = open("transactions.txt", "w")
for i in range(0,32):
    tx_blk.write(Tx.gen_random_tx(q, p, g))
tx_blk.close()

# Test I
# Check all your transactions in a block
ReturnCode = CheckBlock("transactions.txt", q, p, g)
if ReturnCode == -10000:
    print("File Problem")
elif(ReturnCode < 0):
    print("Signtature Problem in Tranaction number", -ReturnCode)
elif ReturnCode == 0:
    print("All Transactions Verify")
else:
    print("Unexpected branching")

# This is for generating a PoW for the block in transactions.txt
# You should have a function called "PoW" in file PoW.py
PoWLen = 5   # The number of 0 hexadecimal digits; i.e. PoWLen = x/4
block = PoW.PoW(PoWLen, q, p, g, "transactions.txt")
f = open("block.txt", "w")
f.write(block)
f.close()
    
# Test II
# Check PoW
f = open("block.txt", "r")
block = f.readlines()
block = "".join(block)
blockHash = hashlib.sha3_256(block.encode('UTF-8')).hexdigest()
if blockHash[0:PoWLen] == "0"*PoWLen:
    print("Proof-of-Work test: passed")
else:
    print("Proof-of-Work test: failed")    
print("hash of the block: ",  blockHash)
