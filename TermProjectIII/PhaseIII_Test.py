#########################################
##  Do not change this file            ##
## Your codes must work with this file ##
#########################################

import math
import random
import string
import warnings
import pyprimes
# These are the modules needed for elliptic curve cryptography
from ecpy.curves import Curve,Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.ecdsa import ECDSA
from ecpy.formatters import decode_sig, encode_sig
######
import TxECDSA       # You have to submit this file, which is the new version that works with ECDSA 
import PoWECDSA      # You have to submit this file, which is the new version that works with ECDSA   
import ChainGen      # You have to submit this file  
import os.path
import hashlib
import sys

if sys.version_info < (3, 6):
    import sha3

def random_string(size=6, chars=string.ascii_uppercase + string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def CheckBlock(filename, curve):
    if os.path.isfile(filename):
        f = open(filename, "r")
        block = f.readlines()
        if len(block)%9 != 0:
            print("Incorrect file format")
            f.close()
            return -10000
        block_count = len(block)//9
        for i in range(0, block_count):
            # coordinates of the public key point
            x1 = int(block[i*9+2][22:-1])
            y1 = int(block[i*9+3][22:-1])
            r = int(block[i*9+7][15:-1])
            s = int(block[i*9+8][15:-1])
            tx = "".join(block[i*9: i*9+7])
            # For the signature verfication
            payer = ECDSA()
            payer_pk = ECPublicKey(Point(x1, y1, curve))
            signature = encode_sig(r, s)
            try:
                assert(payer.verify(tx.encode('UTF-8'), signature, payer_pk))
                ver = 0
                f.close()
                return ver
            except:
                ver = -i-1
                f.close()
                return ver
        return 0
    else:
        print("File does not exist")
        return -10000

##############        
# Student Part

# This is for generating random transactions
# You should have a function with the name "Tx.gen_random_tx()" in "Tx.py"
curve = Curve.get_curve('secp256k1') # The curve used for signing bitcoin transactions 
tx_blk = open("transactions.txt", "w")
for i in range(0,32):
    tx_blk.write(TxECDSA.gen_random_tx(curve))
tx_blk.close()

# Test I
# Verify the signatures of all your transactions in a block
ReturnCode = CheckBlock("transactions.txt", curve)
if ReturnCode == -10000:
    print("File Problem")
elif(ReturnCode < 0):
    print("Signtature Problem in Transaction number", -ReturnCode)
elif ReturnCode == 0:
    print("All transactions verify")
else:
    print("Unexpected branching")


# This is for generating a PoW for the block in transactions.txt
# You should have a function called "PoW" in file PoW.py
PoWLen = 3   # The number of 0 hexadecimal digits; i.e. PoWLen = x/4
block = PoWECDSA.PoW(PoWLen, "transactions.txt")
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
f.close()

# Test III
# Generate the blockchain
BlockLen = 2   # number of transactions in a block
ChainLen = 4    # number of blocks
filename = "Block"
ctr = 0
# block candidate contains only the transactions; not Previous Hash nor PoW
block_candidate = TxECDSA.gen_random_tx(curve)
for j in range(0, BlockLen):
    block_candidate += TxECDSA.gen_random_tx(curve)
PrevBlock = ChainGen.AddBlock2Chain(PoWLen, 0, block_candidate)
f = open(filename + "0.txt", "w")
f.write(PrevBlock)
f.close()
for i in range(1, ChainLen):
    block_candidate = TxECDSA.gen_random_tx(curve)
    for j in range(0, BlockLen):
        block_candidate += TxECDSA.gen_random_tx(curve)
    NewBlock = ChainGen.AddBlock2Chain(PoWLen, PrevBlock, block_candidate)
    f = open(filename + str(i) + ".txt", "w")
    f.write(NewBlock)
    f.close()
    PrevBlock = NewBlock

# Check the blockchain
# First block
chck = 0
f = open(filename + "0.txt", "r")
block = f.readlines()
NewHash = hashlib.sha3_256("".join(block).encode('UTF-8')).hexdigest()
# Check the Pow for the current block
if NewHash[0:PoWLen] != "0"*PoWLen:
    print("PoW error in block no 0")
    chck += 1
f.close()
PrevHash = NewHash
for i in range(1, ChainLen):
    f = open(filename + str(i) + ".txt", "r")
    block = f.readlines()
    if(PrevHash != block[-2][15:-1]):
        print("The current block does not include the hash of the previous block")
        chck += 1
    NewHash = hashlib.sha3_256("".join(block).encode('UTF-8')).hexdigest()
    if NewHash[0:PoWLen] != "0"*PoWLen:
        print("PoW error in block no " + str(i))
        chck += 1
    f.close()
    PrevHash = NewHash
if chck == 0:
    print("Blockchain test: passed")
else:
    print("Blockchain test: failed")
