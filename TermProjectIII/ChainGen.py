import PoWECDSA
import hashlib


def AddBlock2Chain(PoWLen, PrevBlock, block_candidate):
    previous_Hash = 0
    if PrevBlock == 0:
        previous_Hash = str(b'0')
    else:
        previous_Hash = hashlib.sha3_256(PrevBlock.encode('UTF-8')).hexdigest()
    block = PoWECDSA.PoW(PoWLen, "", block_candidate + "Previous Hash: " + previous_Hash + "\n")
    return block