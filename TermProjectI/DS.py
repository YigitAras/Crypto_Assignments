#!/home/yigitaras/anaconda3/envs/cryptoenv/bin/python3
from Crypto.Util import number
# the generation of the prime number is done by PyCrypto library
import math
import os
import random
import string
from Crypto.Hash import SHA3_256


def random_string(size=6, chars=string.ascii_uppercase + string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


class PubParam:
    def __init__(self, qq, pp, gg):
        # if a g value is given that means we have the values
        if gg is not None:
            self.p = pp
            self.q = qq
            self.g = gg
        # if g is not given we have to create our own values
        else:
            # get the sizes of P and Q that are requested
            np = number.size(pp)
            nq = number.size(qq)
            # create the Q first since we will use it first to construct everything else
            self.q = number.getPrime(nq)
            # get a random number which will if multiplied with Q will result in 2**np number
            T = number.getRandomNBitInteger(np-nq)
            # check while T*Q + 1 is not prime and not size of np
            while True:
                # create the T and test again
                T = number.getRandomNBitInteger(np-nq)
                # create the P
                self.p = self.q * T + 1
                if number.isPrime(self.p) and number.size(self.p) == np:
                    break



            self.g = 1
            # keep on checking until G is not 1
            while self.g == 1:
                h = number.getRandomRange(2, self.p-1)
                self.g = pow(h, (self.p-1)//self.q, self.p)

# read from the pubparams.txt file if exists otherwise create one and use those
def GenerateOrRead(file):
    if os.path.isfile(file):
        f = open("pubparams.txt", "r")
        q = int(f.readline())
        p = int(f.readline())
        g = int(f.readline())
        f.close()
        pp = PubParam(q, p, g)
    else:
        pp = PubParam(2**224, 2**2048, None)
        f = open("pubparams.txt","w")
        f.write(str(pp.q)+"\n")
        f.write(str(pp.p)+"\n")
        f.write(str(pp.g))
        f.close()
    return pp.q, pp.p, pp.g

#generate the Keys from Q P G with provided formlas
def KeyGen(Q, P, G):
    alpha = number.getRandomRange(1, Q)
    beta = pow(G, alpha, P)
    return alpha, beta


# Sign the message
def SignGen(m, Q, P, G, alpha):
    k = number.getRandomRange(1, Q)
    # decode the m's utf-8 encoding
    m = m.decode('utf-8')
    hsh = SHA3_256.new()
    r = pow(G, k, P)
    temp = str(m) + str(r)
    hsh.update(bytes(temp, 'utf-8'))
    h = int(hsh.hexdigest(), 16)
    s = (alpha*h + k) % Q 
    return s,h


# check the signature
def SignVer(m, s, h, q, p, g, beta):
    # v1 = g^s mod p
    v1 = pow(g, s, p)
    # decode the m's utf-8 encoding
    m = m.decode('utf-8')
    # minus_beta is BETA inverse
    minus_beta = modinv(beta, p)
    # B2 is BETA^-h mod p
    b2 = pow(minus_beta, h, p)
    # v_fin = v1*b2 mod p where v_fin = (g^s * BETA^-h) mod g
    v_fin = (v1*b2) % p
    hsh = SHA3_256.new()
    # create the has of m||v_fin
    hsh.update(bytes((str(m)+str(v_fin)).encode('utf-8')))
    h_tilda = int(hsh.hexdigest(), 16)
    # check h_tilda and h
    if (h % q) == (h_tilda % q):
        return 0
    else:
        return -1


