import random
import warnings
import pyprimes
import DS
import sys


##############
# Student Part
# Test your public parameters with this routine
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

    r = (p - 1) % q
    if (r != 0):
        return -3

    k = (p - 1) // q

    x = pow(g, k, p)
    if (x == 1):
        return -4
    y = pow(g, q, p)
    if (y != 1):
        return -4

    return 0


# Test your key pair
def CheckKeys(q, p, g, alpha, beta):
    if beta == pow(g, alpha, p):
        return 0
    else:
        return -1


# Test your signature algorithm with a random message
def CheckSignature(q, p, g, alpha, beta):
    message = DS.random_string(random.randint(32, 512)).encode('UTF-8')
    (s, h) = DS.SignGen(message, q, p, g, alpha)
    return DS.SignVer(message, s, h, q, p, g, beta)


def CheckTestSignatures():
    f = open("TestSet.txt", "r")
    q = int(f.readline())
    p = int(f.readline())
    g = int(f.readline())
    beta = int(f.readline())
    for i in range(0, 10):
        message = f.readline().rstrip("\n")
        s = int(f.readline())
        h = int(f.readline())
        ReturnCode = DS.SignVer(message.encode('UTF-8'), s, h, q, p, g, beta)
        if ReturnCode != 0:
            f.close()
            return -1
    f.close()
    return 0


##### This part executes
# Generate or read the public parameters
# You need to have a routine named GenerateOrRead that reads q, p, g from "pubparams.txt" if exists
# Otherwise, it should generate public parameters and write them to "pubparams.txt"
(q, p, g) = DS.GenerateOrRead("pubparams.txt")
# DS.GenerateTestSignatures(q, p, g)  # Generate sample signatures (Students do not uncomment this)

# Testing part
# Test public parameters
ReturnCode = checkDSparams(q, p, g)
if ReturnCode == 0:
    print("Public parameters: Passed!")
elif ReturnCode == -1:
    print("q is not prime")
    sys.exit()
elif ReturnCode == -2:
    print("p is not prime")
    sys.exit()
elif ReturnCode == -3:
    print("q does not divide p")
    sys.exit()
elif ReturnCode == -4:
    print("g is not a generator")
    sys.exit()

(alpha, beta) = DS.KeyGen(q, p, g)  # generate key pair
ReturnCode = CheckKeys(q, p, g, alpha, beta)
if ReturnCode == 0:
    print("Public/private key pair: Passed!")
else:
    print("Public/private key pair: Failed!")
    sys.exit()

ReturnCode = CheckSignature(q, p, g, alpha, beta)

if ReturnCode == 0:
    print("Signature generation: Passed!")
else:
    print("Signature generation: Failed!")
    sys.exit()

if (CheckTestSignatures() == 0):
    print("Sample signature test: Passed!")
else:
    print("Sample signature test: Failed!")

