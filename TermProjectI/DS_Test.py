import math
import random
import string
import warnings
import pyprimes
import DS
import os.path

def random_string(size=6, chars=string.ascii_uppercase + string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# Erkay Savas (ES): This is for me to generate or read the public parameters
def GenerateOrRead():
    if os.path.isfile("pubparams.txt"):
        f = open("pubparams.txt", "r")
        q = int(f.readline())
        p = int(f.readline())
        g = int(f.readline())
        f.close()
        pp = DS.PubParam(q, p, g)
    else:
        pp = DS.PubParam(2**224, 2**2048, None)
        f = open("pubparams.txt","w")
        f.write(str(pp.q)+"\n")
        f.write(str(pp.p)+"\n")
        f.write(str(pp.g))
        f.close()
    return pp.q, pp.p, pp.g

def GenerateTestSignatures(q, p, g):
    f = open("TestSet.txt","w")
    f.write(str(q)+"\n")
    f.write(str(p)+"\n")
    f.write(str(g)+"\n")
    (alpha, beta) = DS.KeyGen(q, p, g)
    f.write(str(beta)+"\n")
    for i in range(0, 10):
        message = random_string(random.randint(32, 512))
        (s, h) = DS.SignGen(message.encode('UTF-8'), q, p, g, alpha)
        f.write(message+"\n")
        f.write(str(s)+"\n")
        f.write(str(h)+"\n")
    f.close()    
    return 0    
    
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

# Test your key pair
def CheckKeys(q, p, g, alpha, beta):
    if beta == pow(g, alpha, p):
        return 0
    else:
        return -1

# Test your signature algorithm with a random message
def CheckSignature(q, p, g, alpha, beta):
    message = random_string(random.randint(32, 512)).encode('UTF-8')
    (s, h) = DS.SignGen(message, q, p, g, alpha)
    return DS.SignVer(message, s, h, q, p, g, beta)

def CheckTestSignatures():
    f = open("TestSet.txt", "r")
    q = int(f.readline())
    p = int(f.readline())
    g = int(f.readline())
    beta = int(f.readline())
    for i in range(0,10):
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
(q, p, g) = GenerateOrRead()  # Generate or read the public parameters
GenerateTestSignatures(q, p, g)  # Generate sample signatures

# Testing part
# Test public parameters
ReturnCode = checkDSparams(q, p, g)
if ReturnCode == 0:
    print("Public parameters: Passed!")
elif ReturnCode == -1:
    print("q is not prime")
elif ReturnCode == -2:
    print("p is not prime")
elif ReturnCode == -3:
    print("q does not divide p")
elif ReturnCode == -4:
    print("g is not a generator")
    
(alpha, beta) = DS.KeyGen(q, p, g) # generate key pair
ReturnCode = CheckKeys(q, p, g, alpha, beta)
if ReturnCode == 0:
    print("Public/private key pair: Passed!")
else:
    print("Public/private key pair: Failed!")

ReturnCode = CheckSignature(q, p, g, alpha, beta)

if ReturnCode == 0:
    print("Signature generation: Passed!")
else:
    print("Signature generation: Failed!")

if (CheckTestSignatures() == 0):
    print("Sample signature test: Passed!")
else:
    print("Sample signature test: Failed!")
    
