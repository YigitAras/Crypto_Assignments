# Run "pip install ecpy" if ecpy is not installed
import random
import hashlib
import sys
import string
from ecpy.curves import Curve,Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.ecdsa import ECDSA
from ecpy.formatters import decode_sig, encode_sig

if sys.version_info < (3, 6):
    import sha3

curve = Curve.get_curve('secp256k1')
n = curve.order
P = curve.generator
sA = random.randint(0,n)
sk = ECPrivateKey(sA, curve)
QA = sA*P
pk = ECPublicKey(QA)

signer = ECDSA()

message = b'Anything goes here'

sig = signer.sign(message, sk)

(r, s) = decode_sig(sig)

f = open("deneme.txt", "w")
f.write("Public key - x: " + str(QA.x)+"\n")
f.write("Public key - y: " + str(QA.y)+"\n")
f.write("Signature - r: " + str(r)+"\n")
f.write("Signature - s: " + str(s)+"\n")
f.close()

f = open("deneme.txt", "r")
x1 = int(f.readline()[16:-1])
y1 = int(f.readline()[16:-1])
r1 = int(f.readline()[15:-1])
s1 = int(f.readline()[15:-1])
f.close()

verifier = ECDSA()
pk1 = ECPublicKey(Point(x1, y1, curve))
sig1 = encode_sig(r1, s1)

message = b'Anything goes here'
try:
    assert(verifier.verify(message,sig1, pk1))
    print("Signature verifies")
except:
    print("Signature does not verify")
    
message = b'Anything goes heree'
try:
    assert(verifier.verify(message,sig1, pk1))
    print("Signature verifies")
except:
    print("Signature does not verify")
    
