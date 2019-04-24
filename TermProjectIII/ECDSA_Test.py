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

# You can keep this part (i.e., curve setting and key generation)
curve = Curve.get_curve('secp256k1')
n = curve.order
P = curve.generator
sA = random.randint(0, n)
sk = ECPrivateKey(sA, curve)
QA = sA*P
pk = ECPublicKey(QA)

# You need to change sign and verify methods below
signer = ECDSA()  # this line can be removed
message = b'Anything goes here'
sig = signer.sign(message, sk)  # new sign method here

verifier = ECDSA() # this line can be removed

message = b'Anything goes here'
try:
    assert(verifier.verify(message, sig, pk)) # new sign method here
    print("Signature verifies")
except:
    print("Signature does not verify")
    
message = b'Anything goes heree'
try:
    assert(verifier.verify(message, sig, pk)) # new sign method here
    print("Signature verifies")
except:
    print("Signature does not verify")
