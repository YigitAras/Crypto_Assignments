import hashlib


def PoW(PoWLen, filename, blk=None):
    # necessary length below
    x_len = PoWLen * 4

    # open file and read the block
    nonce = 0

    if blk is None:
        f = open(filename, "r")
        block = f.readlines()
        block = "".join(block) + "Nonce: "
    else:
        block = "".join(blk) + "Nonce: "

    while True:
        blockHash = hashlib.sha3_256((block + str(nonce) + "\n").encode('UTF-8')).hexdigest()
        if blockHash[0:PoWLen] == "0" * PoWLen:
            block = block + str(nonce) + "\n"
            return block
        nonce = nonce + 1
