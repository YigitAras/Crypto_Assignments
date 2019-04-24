from ecpy.curves import Curve,Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.ecdsa import ECDSA
from ecpy.formatters import decode_sig, encode_sig
from Crypto.Util import number as Num


def gen_random_tx(curve):
    # get a random 128 BIT integer for serial number
    serial_num = Num.getRandomNBitInteger(128)

    # create the public key for sender
    n = curve.order
    P = curve.generator
    sA = Num.getRandomRange(0, n+1)
    sK = ECPrivateKey(sA, curve)
    QA = sA*P
    pk = ECPublicKey(QA)

    signer = ECDSA()

    # create the public key for sendee
    sA_2 = Num.getRandomRange(0, n+1)
    sK_2 = ECPrivateKey(sA_2, curve)
    P2 = curve.generator
    QA_2 = sA_2*P2
    pk_2 = ECPublicKey(QA_2)

    # header for the block
    temp = "*** Bitcoin transaction ***\n"

    # add the serial number to the block
    temp = temp + "Serial number: " + str(serial_num) + "\n"
    # write payers public keys
    temp = temp+"Payer public key - x: " + str(QA.x) + "\n"
    temp = temp+"Payer public key - y: " + str(QA.y) + "\n"
    # write payees public keys
    temp = temp+"Payee public key - x: " + str(QA_2.x)+ "\n"
    temp = temp+"Payee public key - y: " + str(QA_2.y)+ "\n"

    # get random transaction val
    amount = Num.getRandomRange(0,1000001)
    temp = temp+ "Amount: " + str(amount) + "\n"

    sig = signer.sign(temp.encode("utf-8"), sK)
    (r, s) = decode_sig(sig)
    temp = temp + "Signature (r): " + str(r) + "\n"
    temp = temp + "Signature (s): " + str(s) + "\n"

    return temp
