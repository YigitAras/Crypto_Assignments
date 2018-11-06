#!/home/yigitaras/anaconda3/bin/python3
from hw03 import *
import itertools
from functools import reduce

# constants used in the multGF2 function
mask1 = mask2 = polyred = None


def setGF2(degree, irPoly):
    """Define parameters of binary finite field GF(2^m)/g(x)
       - degree: extension degree of binary field
       - irPoly: coefficients of irreducible polynomial g(x)
    """

    def i2P(sInt):
        """Convert an integer into a polynomial"""
        return [(sInt >> i) & 1
                for i in reversed(range(sInt.bit_length()))]

    global mask1, mask2, polyred
    mask1 = mask2 = 1 << degree
    mask2 -= 1
    polyred = reduce(lambda x, y: (x << 1) + y, i2P(irPoly)[1:])


def multGF2(p1, p2):
    """Multiply two polynomials in GF(2^m)/g(x)"""
    p = 0
    while p2:
        if p2 & 1:
            p ^= p1
        p1 <<= 1
        if p1 & mask1:
            p1 ^= polyred
        p2 >>= 1
    return p & mask2


def Question1():
    # x^6 + x^5 + 1 is our primitive
    print("#####################ANSWER TO THE FIRST QUESTION:#######################################")
    p1 = [1, 0, 0, 0, 0, 1, 1]
    start = [1, 0, 0, 0, 0, 0]
    test = [1, 0, 0, 0, 0, 0]
    out = []
    out.append(LFSR(p1, start))
    counter = 1
    while start != test:
        out.append(LFSR(p1, start))
        counter += 1
    print("First output period is:")
    print(out)
    print("It has {} elements".format(len(out)))
    print("Since FindPeriod() of it returns {}".format(FindPeriod(out)))
    print("We can say it is a PRIMITIVE")
    print("\n")
    print(
        "************************************************************************************************************************************************")
    print("\n")


print("\n")


def Question2():
    print("##############################ANSWER TO THE SECOND QUESTION##########################################")
    ex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1,
          0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1]
    ses = BM(ex)
    print("Shortest LFSR using BM function is:(ones representing the active ones)")
    print("Length of:{}".format(len(ses)))
    print(ses[1])
    print("1+ x^4 + x^6 + x^8 + x^11")
    print(
        "*************************************************************************************************************************************************")
    print("\n")


print("\n")


def Question3():
    print("##################################ANSWER TO THE THIRD QUESTION#######################################")
    enc = [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
           0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
           1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0,
           1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0,
           1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1,
           1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1,
           1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
           1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0,
           1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
           1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0,
           0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1,
           0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1,
           0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0,
           1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
           1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1,
           1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0,
           0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1,
           1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0]

    msg = "Dear Student"
    msg_bin = ASCII2bin(msg)
    stream = [int(bool(msg_bin[i] != bool(enc[i]))) for i in range(len(msg_bin))]
    # GET THE MINIMUM PRIM POLY
    ans = BM(stream)[1]
    states = list(itertools.product([0, 1], repeat=11))

    for state in states[1:]:
        state = list(state)
        key = []
        while len(key) != len(stream):
            key.append(LFSR(ans, state))
        if key == stream:
            while len(key) != len(enc):
                key.append(LFSR(ans, state))
            print("Key is :")
            print(key)
            break
    print("Answer in binary: ")
    answer = [int(bool(key[i]) != bool(enc[i])) for i in range(len(enc))]
    print(answer)
    print("Answer in ASCII is:")
    print(bin2ASCII(answer))
    print("\n")
    print(
        "**********************************************************************************************************************************")
    print("\n")
    print("\n")


def Question4():
    # Define binary field GF(2^8)/x^8 + x^4 + x^3 + x + 1
    setGF2(8, 0b100011011)
    # Evaluate the product (x^7+x^6+x^4+x^2)(x^7+x^3+x^2+x+1)
    ses = multGF2(0b11010100, 0b10001111)
    val = format(ses, "b")
    val = list(val)
    print("Multiplication of x^7+x^6+x^4+x^2 and x^7+x^3+x^2+x+1 in GF(2^8)")
    print("With field created by GF(2^8) -> x^8+x^4+x^3+x+1")
    print("Result is:")
    print(val)
    print("x^7+x^6+x^4+x^3+1")
    ses = multGF2(0b11010100, 0b11000101)
    val = format(ses, "b")
    val = list(val)
    print("To show that x^7+x^6+x^4+x^2 and x^7+x^6+x^2+1 are inverses in GF(2^8) given above,")
    print("We multiply them and if the result is 1 they are inverses,")
    print("Result of multiplication is:")
    print(val)
    print("Since the result is 1 as shown just above, they are inverses...")
    print("***********************************************************************************")
    print("\n")
    print("\n")


def Question5():
    print(
        "####################################### ANSWER TO FIFTH QUESTION ############################################################")
    print("\n")
    print(
        "Without the ShiftRow and Mixcolumn layers, we lose the diffusion property and there will be a one byte to one byte correspondance from plaintext to ciphertext")
    print(
        "This will result in the encrpytion becoming 16 substitution ciphers with size 8. We can select a chosen plaintext with the plain texts with same values such as:")
    print(" p =[0,0,.......0] or p_a = [1,1,1,1,....,1] , ... , p_last=[255,255,.....,255]")
    print(
        "*******************************************************************************************************************************")
    print("\n")
    print("\n")


Question1()
Question2()
Question3()
print("################################### ANSWER TO THE FOURTH QUESTION #######################################")
Question4()
Question5()