#!/home/yigitaras/anaconda3/bin/python3

"""
Solutions for HW01 
"""
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 
'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 
'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 
'Z': 0.07}
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

def gcd(a,b):
    while b!=0:
        c = a%b
        a=b
        b=c
    return a

def phi(n):
    x = 0
    for i in range(1,n+1):
        if(gcd(n,i)==1):
            x += 1
    return x
# ********************** </HELPER FUNCTIONS> **************************************


# ********************** <QUESTION FUNCTIONS> *************************************
def Question1(word):
    print("-"*60)
    print("ANSWER FOR QUESTION 1: ")
    print("-"*60)
    # ASCII OF A-Z 65-90
    word = word.upper()
    def subs(char,amount):
        if ord(char)>=65 and ord(char)<=90:
            char_num = ord(char)-65
            char = chr((char_num+amount)%26+65)
        return char
    for i in range(1,26):
     
        print("Shift amount: {}, Word: {}".format(i, ''.join(subs(ch, i) for ch in word)))


# HINT : most frequent is E
def Question2(sentence,freq):
    print("-"*60)
    print("ANSWER FOR QUESTION 2: ")
    print("-"*60)
    ref_dict = dict()
    for ch in sentence:
        ref_dict[ch] = ref_dict.get(ch,0)+1
    sort_dict = sorted(ref_dict.items(), key=lambda kv: kv[1],reverse=True)   
    top_vals = []
    counter = 0
    for k,v in sort_dict:
        if counter > 5:
            break
        top_vals.append(k)
        counter += 1
    # m * X(88-65) + b = E(69-65) mod 26
    # b --> 1-25  |  m - > 1-25
    C = ord(top_vals[0])-65
    P = ord(freq)-65
    encrypt_list = list()
    for m in range(1,25):
        b = (P - C*m)%26
        # Dont add to list if it doesnt have inverse
        g, x, y = extended_gcd(m, 26)
        if g == 1:
            encrypt_list.append((m,b))
    decrypt_list = list()

    def decrypt(ch,a,b):
        return chr(((((ord(ch)-65)*19)+b) % 26)+65)
    def encrypt(ch,a,b):
        return chr(((((ord(ch)-65)-b) * a) %26)+65)
    # GOOD LIST CONTAINS POSSIBLE KEY VALUE COMBINATIONS
    for mul,add in encrypt_list:
        temp = ''.join(decrypt(ch,mul,add) for ch in sentence)
        if temp is not sentence:
            print("Dec Keys:{},{}".format(mul,add))
            print("{}\n".format(temp))
            print(40*'*')
    dec_mul = int(input("Please enter the 1st Dec Key from key pair with meaningful translation from above decryptions:\n").rstrip())
    dec_add = 0
    for i in range(1,26):
        inv = modinv(dec_mul,26)
        if  ((P*inv)+ i)%26 == C:
            dec_add = i
            break
    print("\nEncryption Keys: {}, {}".format(inv,dec_add))
    print("Meaningful translated block of text from above is the Plaintext\n")


def Question3():
    print("-"*60)
    print("ANSWER FOR QUESTION 3: ")
    print("-"*60)
    var = 26*26*26*26
    print("*"*60)
    print("Number of quadgrams is: {}".format(var))
    print("Thus the modulus is: {}".format(var))
    print("Key space is then totient_function({}) * {}".format(var,var))
    phi_res = phi(var)
    print("So the key space is {}".format(phi_res*var))
    print("*"*60)

def Question4():
    print("-"*60)
    print("ANSWER FOR QUESTION 4: ")
    print("-"*60)
    print("*"*60)
    print("Statistics for 4-letter words still hold for languages,")
    print("so it is not safe from language statistics")
    print("*"*60)

def Question5(cipher_text,key_vec,ind):
    if ind ==1:
        print("-"*60)
        print("ANSWER FOR QUESTION 5: ")
        print("-"*60)
    # Slide through the text with key
    k_l = len(key_vec)
    k_c = 0
    plain_text = ""
    for ch in cipher_text:
        plain_text += chr((((ord(ch)-65)-(ord(key_vec[k_c])-65))%26)+65)
        k_c = (k_c+1)%(k_l)
    print("The decrypted plain text is:\n{}".format(plain_text))

def Question6():
    print("-"*60)
    print("ANSWER FOR QUESTION 6: ")
    print("-"*60)
    # READ THE TEXT FILE AND PARSE IT PROPERLY FOR DECRYPTION
    handler = open("bonus_var.txt","r")
    cipher_text = ""
    for line in handler:
        for ch in line:
            if ch.isalpha() == True:
                    cipher_text += ch.upper()

    index = len(cipher_text)
    collision_dict = dict()
    for i in range(1,13):
        num_of_cols = 0
        for j in range(0,index):
            if j+i <= index-1:
                if cipher_text[j] == cipher_text[j+i]:
                    num_of_cols += 1
            else:
                break
        collision_dict[i] = num_of_cols
    s_val = sorted(collision_dict.items(), key=lambda kv: kv[1],reverse=True)
    possible_keys = []
    counter= 0
    for k,v in s_val:
        if counter>=3:
            break
        possible_keys.append(k)
        counter += 1
    # POSSIBLE KEYS CONTAIN THE POSSIBLE KEY LENGHTS NOW
    best_candid = possible_keys[0]
    best_keys = []
    best_keys2=[]
    for i in range(0,best_candid):
        temp = cipher_text[i::best_candid]
        freq_dict = dict()
        for ch in temp:
            freq_dict[ch] = freq_dict.get(ch,0)+1
        s_freq = sorted(freq_dict.items(),key=lambda kv: kv[1],reverse=True)
        suicide_list = list()
        suicide_list2=list()
        ctr = 0
        for k,v in s_freq:
            if ctr==4:
                break
            suicide_list.append((k,v))
            suicide_list2.append(k)
            ctr += 1
        best_keys.append(suicide_list)
        best_keys2.append(suicide_list2)
    most_freq = ["E","T","A","O","I","N"] # in English Alphabet
    print("-"*60)
    print("Following is the Top 4 letters in the cipher text for each possible key vector blocks with their respective number of occurences:")
    for item in best_keys:
        print(item)
    print("-"*60)
    vector_key = 0
    answer_vec = []
    for item in best_keys2:
        z = len(item)
        shift = 0
        my_dic = dict()
        for i in range(0,z):
            temp = list()
            total_prob = 1
            shift = (((ord(item[i])-65)-(ord("E")-65))%26)
            for ch in item:
                dec = chr(((ord(ch)-65-shift)%26)+65)
                temp.append(dec)
                total_prob *= englishLetterFreq[dec]
            print("For Vec_Key[{}], assuming {} was shifted from E and possible Dec_Key: {} with likelihood {}".format(vector_key,item[i],chr(shift+65),total_prob))
            print(temp)
            my_dic[chr(shift+65)] = total_prob
        vector_key += 1
        print("Bigger the number for likelihood bigger the chance so select the Dec_Key with biggest likelihood")
        answer_vec.append(my_dic)
        print("*"*60)
    #vec_key = input("Enter the highest likelihood from all the groups as a total key")
    #vec_key = vec_key.upper()
    #Question5(cipher_text,vec_key)
    counter = 0
    ans_str = ""
    for diction in answer_vec:
        sorted_dict = sorted(diction.items(),key=lambda kv: kv[1],reverse=True)
        top = sorted_dict[0][0]
        top_val = sorted_dict[0][1]
        print("From Group {}: Key {} with highest likelihood {}".format(counter,top,top_val))
        ans_str += top
        counter +=1
    print("Key with highest probability: {} with length {}".format(ans_str,len(ans_str)))
    print("Decrypting the cipher text......")
    Question5(cipher_text,ans_str,0)





    





# ********************* </QUESTION FUNCTIONS> *************************************

"""
    **************************************************************************************
    *   QUESTION FUNCTION CALLS, RUN THE SCRIPT TO SEE THEIR EFFECTS 1-by-1              *             
    *   FOLLOW THE INSTRUCTION AND ENTER VALUES ASKED FOR WHEN PROMPTED                  * 
    **************************************************************************************
"""
# *****************************************************************************

Question1("DCT")

# *****************************************************************************

Question2("QRGHFSPVSDGHFMXIDKMXIXFGFHFSBFSQXMXVGKDJXMQRGSDGMXIXFGXM",'E')

# *****************************************************************************

Question3()

# *****************************************************************************

Question4()

# *****************************************************************************

Question5("WADYZMHLTQPSWARRTIGNXCFLWARMHIFNYBAZSELEMMBOFRQBDRNRURUQTDRIFRYRDIGHWRE","ONLYME",1)

# *****************************************************************************

Question6()

# *****************************************************************************