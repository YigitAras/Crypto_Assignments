#!/home/yigitaras/anaconda3/bin/python3
import math
from math import gcd
import fractions
import random
import timeit
import time
from collections import deque


#import pyprimes
#import warnings
# ********************** <HELPER FUNCTIONS> ***************************************
# GCD 
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
# mod inverse
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		return None
	return x % m

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

def phi_list(n):
	x = []
	for i in range(1,n+1):
		if gcd(n,i) == 1 :
			x.append(i)
	return x


small_primes = [2, 3, 5, 7, 11, 13]

def BasicTest(n, q, k):
    a = random.randint(2, n-1)
    x = pow(a, q, n)
    if x == 1 or x == n-1:
            return 1
    for i in range(1, k):
        x = pow(x,2,n)
        if x == 1:
            return -1
        if x == n-1:
            return 1        
    return -1

def MRTest(n, t):
    k = 0
    q = n-1
    while (q%2==0):
        q = q//2
        k+=1
    while (t>0):
        t = t-1
        if BasicTest(n, q, k)==1:
            continue
        else:
            return -1
    return 1    

def PrimalityTest(n,t):
    for i in small_primes:
        if n%i==0:
            return -1
    else:
        if MRTest(n, t) == 1:
        	return True
        elif MRTest(n,t) == -1:
        	return False

# *******************  </HELPER FUNCTIONS> ****************************************


# --------------------------------- QUESTION 1 ------------------------------------------------------------------

def Question1():
	print("*********************************************************************************************+")
	print("ANSWERS TO THE QUESTION 1:")
	n = 7519197963616825059473475919665272935688024085617838056506345489899068679826922644904433165878890900819649430009054548164262464489216932204311933941987267253245684421002477067674284279907689858948515642332083283659312231907446846847748777699985285177717295366767158551808673171192059742572047913270325915613

	y = 3209914600874008500669935401430665363662412488153089828835443261030801437200212347910860119033606488561197004601674106596598459681203418060565894194568759290922801528229679761127331866325136546667744322264558258342327040988162854318186593925780283235229957993222433235872039468178675216535512488042635755042

	sq1 = 3708938308454104516702151825577264734932704619196334493742102012085049133860066916102730058438177755140779946753156246803295551884416938289763313330523905172072027042248481556236130811168223100218388139803554641018491672049531817488615769186936860939150325755164461297959399070505580168312640786987386537970

	sq2 = 3810259655162720542771324094088008200755319466421503562764243477814019545966855728801703107440713145678869483255898301360966912604799993914548620611463362081173657378753995511438153468739466758730127502528528642640820559857915029359133008513048424238566969611602697253849274100686479574259407126282939377643

	sq3 = 1204281249197785714266442632825140385815760158008253320866738851601057451123077855202576520382301531140434905065394058045630903820174243044223260732733986914562762640400496995411532307823305824643456122585957628552765307683540837887390010934716580867984045247189957418104618386361581534738350103893735668456

	sq4 = 6314916714419039345207033286840132549872263927609584735639606638298011228703844789701856645496589369679214524943660490118631560669042689160088673209253280338682921780601980072262751972084384034305059519746125655106546924223906008960358766765268704309733250119577201133704054784830478207833697809376590247157

	p = gcd(sq1-sq3,n)
	q = n/p
	print("P is as follows:")
	print(int(p))
	print("\n")
	print("Q is as follows:")
	print(int(q))
	print("\n\n")

# --------------------------------- QUESTION 2 -------------------------------------------------------------------
def Question2(n):
	print("********************************************************************************************")
	print("ANSWER TO THE QUESTION 2")
	group_list = phi_list(n)
	print(" The elements in group Z_{},and there are {} of them:".format(n,len(group_list)))
	print(group_list)
	print("")
	#--------------------------------------
	list_of_generators = list()
	for no in group_list:
		ses = list()
		for i in range(1,n**2):
			res = pow(no,i,n)
			if res == 1:
				ses.append(res)
				break
			ses.append(res)
		if len(ses) == len(group_list):
			list_of_generators.append(no)

	print("The generators in group Z_{},since it is a cyclic group,there are {}:".format(n,len(list_of_generators)))
	print(sorted(list_of_generators))
	print("")
	# --------------------------------------
	quad = list()
	for i in group_list:
		resul = (i*i) % n
		quad.append(resul)
	quad = set(quad)

	ex = list()
	for item in quad:
		if gcd(item,n) ==  1:
			ex.append(item)
	print("Quadratic Residues which are relatively prime with {}, QR*_{},there are {}:".format(n,n,len(ex)))
	print(sorted(ex))
	print("\n")
	print("Generators in QR*_{},since their powers generate all elements in QR*_{}:".format(n,n))
	second_generators = list()
	for item in ex:
		ses2 = list()
		for i in range(1,n**2):
			res = pow(item,i,n)
			if res == 1:
				ses2.append(res)
			ses2.append(res)
		if set(ses2) == set(ex):
			second_generators.append(item)
	print(sorted(second_generators))
	print("\n")
	print("**********************************************************************************************")

# --------------------------------- QUESTION 3 -------------------------------------------------------------------
def Question3():
	p = 10106404377238244429826597333701722135807526565404559030730896339579442857374388664504194768519009799965064145557030402164596983123568189834021494235031749
	q = 13163502274590772696691357017188157383494073914454743555560229941893711785933411409679348168803213122008986323048364979277888128708485862429032314868646957

	c = 86558429746256786220797160070602630299194622171442102432718868178774008203963283371082296312613592328933331443800737112868177768290770644915753506516969943009267919574620060086036513229518287908509845029476546407334692827450859273444583008387805272482776780230890488254799112954960574416568539455497347050126
	e =67

	n = p*q 

	resp = PrimalityTest(int(p),10)
	resq = PrimalityTest(int(q),10)
	print("THE ANSWER TO THE QUESTION 3:")
	print("P and Q are primes: {} {}".format(resp,resq))
	print("\n")

	# since P and Q are primes
	phi_n = (p-1)*(q-1)
	# d = e_inv mod phi(n)
	d = modinv(e,phi_n)
	# 
	print("M is : ")
	m = pow(c,d,n)
	print(m)
	print("\n")

	c_p = c % p
	c_q = c % q
	d_p = d %(p-1)
	d_q = d % (q-1)
	p_inv = modinv(p,q)
	q_inv = modinv(q,p)
	c_p_pow_d_p = pow(c_p,d_p,p)
	c_q_pow_d_q = pow(c_q,d_q,q)
	print("C_p is: {}".format(c_p))
	print("C_q is: {}".format(c_q))
	print("d_p is: {}".format(d_p))
	print("d_q is: {}".format(d_q))
	print("p_inv mod q is: {}".format(p_inv))
	print("q_inv mod p is: {}".format(q_inv))
	print("c_p to the power of d_p: {}".format(c_p_pow_d_p))
	print("c_q to the power of d_q: {}".format(c_q_pow_d_q))
	print("\n")
	SOL = (c_p_pow_d_p*q_inv*q+c_q_pow_d_q*p_inv*p ) % n
	print("C to the power d mod n is:")
	print(SOL)
	print("\n")

	times  = 100
	t1 = time.clock()
	for i in range(1,times):
		pow(c,d,n)
	t2 = time.clock()
	regular_exp_time = t2-t1

	t3 = time.clock()
	for i in range(1,times):
		#c_p = c % p
		#c_q = c % q
		#d_p = d %(p-1)
		#d_q = d % (q-1)
		c_p_pow_d_p = pow(c_p,d_p,p)
		c_q_pow_d_q = pow(c_q,d_q,q)
		res = (c_p_pow_d_p*q_inv*q+c_q_pow_d_q*p_inv*p ) % n
	t4 = time.clock()
	crt_exp_time = t4-t3
	print("Without CRT: {}".format(regular_exp_time))
	print("With CRT:  {}".format(crt_exp_time))
	print("CRT is NEARLY(sometimes computer does weird stuff and it drops to 3) 4 times faster than the POW function")
	print("\n")
	print("***********************************************************************")


def Question4():
	n = 876757185537497549441688380876 
	a = 726529482843138430251706107365
	b = 374479581720142608093094131318

	a2=682523910410036363063715440006
	b2=233807680780339430865969182340


	a3=217662435485891894157847112298
	b3=815512939769276810314824385915
	# check solution for ax = b mod n

	# need to check x = b * a^-1 mod n
	print("ANSWER FOR QUESTION 4:")
	d = gcd(a,n)
	d2 = gcd (a2,n)
	d3 = gcd(a3,n)
	print("*****************************************************")
	print("For a = {}".format(a))
	print("d = GCD(a,n)= {}".format(d))
	ans = (int(b) * int(modinv(a,n))) % int(n) 
	print("There is one solution: {}".format(ans))
	print("\n")

	print("*****************************************************")
	print("For a2 = {}".format(a2))
	print("d2 = GCD(a2,n) = {} , there may be solutions...".format(d2))
	print("Can b2 = {} be divided by d2 = {} ? => {}".format(b2,d2,(b2%d2 == 0)))
	print("There will be {} solutions".format(d2))
	a2_div_d2 = int(a2) // int(d2)
	b2_div_d2 = int(b2) // int(d2)
	n_div_d2 = int(n) // int(d2)
	ans2 = (b2_div_d2 * modinv(a2_div_d2,n_div_d2)) % n_div_d2
	ans2_sec = ans2 + n_div_d2
	print("First answer: {}".format(ans2))
	print("Second answer: {}".format(ans2_sec))
	print("\n")

	

	print("****************************************************")
	print("For a3 = {}".format(a3))
	print("d3 = GCD(a3,n) = {}".format(d3))
	print("Can b3 = {} be divided by d3 = {} ? => {}".format(b3,d3,(b3%d3 == 0)))
	print("There is no solution ... since b3 cannot be divided by d3 ...")
	print("\n")

	print("****************************************************")


def Question5():
	print("ANSWER TO THE QUESTION 5:")
	# poly = x^5 + x + 1
	p1 = [1,0,0,0,1]
	# poly2 = x^4 + x^3 + 1
	p2 = [0,0,1,1]
	def full_cycle(given):
		lgt = len(given)
		test = []
		for i in range(0,lgt):
			if given[i] == 1:
				test.append(i)

		start_state = deque([])
		for i in range(0,lgt):
			if i == lgt-1:
				start_state.append(1)
			else:
				start_state.append(0)
		test_state = start_state.copy()
		ctr = 0 
		while True:
			print(list(start_state))
			ctr2 = 0
			isEqual = True
			for i in test:
				if ctr2 == 0:
					ses = start_state[i]
					ctr2 += 1
				else:
					ses = int(not(ses ==start_state[i]))
					ctr2 += 1
			start_state.pop()
			start_state.appendleft(ses)		
			for i in range(0,len(start_state)):
				if test_state[i] != start_state[i]:
					isEqual = False
			ctr = ctr +1
			if isEqual == True:
				print(list(start_state))
				print("Cycles happened: {}".format(ctr))
				break
		if ctr == (lgt**2) -1:
			print("{} does a full cycle so it generates maximum period sequence, its period is {}".format(given,ctr))
		else:
			print("{} does not do a full cycle so it doesn't generate maximum period,its period is {}".format(given,ctr))
	full_cycle(p1)
	print("----------------------------------------------")
	full_cycle(p2)
	print("----------------------------------------------")
	print("So x^5+x+1 doesn't generate maximum period... should have done 2^n-1")
	print("And x^4+x^3+1 does generate maximum period... it did 2^n-1")
	print("**************************************************************************")



	

# *************************** Answer Calls ******************************************
Question1()
Question2(58)
Question3()
Question4()
Question5()
