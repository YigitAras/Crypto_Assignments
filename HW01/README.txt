*****************************************************************************
*                                                                           *
*    Description of the functions in HW1 file                               *
*****************************************************************************

(DISCLAIMER: The printed plaintexts will be just letters back to back without
punctuation or empty spaces for simplicity)

(INSTRUCTION: Run the script to see the answers for every question)


*****************************************************************************
* Question 1                                                                *
*****************************************************************************
1) It will print all the possible shifts of the given parameter (@param),
the meaningful 2 are the answer. In this case "DTK" is given but it works in 
general with any length of param.


*****************************************************************************
* Question 2                                                                *
*****************************************************************************
2)Given the text as param (in this instance the text given in the question) 
with only alphabetical input without spaces or special characthers, the 
function Question2(param,hint) will get two arguments @param and @hint. 
@hint will be the statistically most common letter in the alphabet and the 
function will find most common 3 Letters from the given @param and find out
possible Key Pairs through the a*(plain_text)+ b == (cipher_text) mod 26. 
It will print out the decrypted possible texts. Then you will be asked to 
enter the first key written on top of the meaningful decrypted texts. 
Write it and you will recieve the encryption keys and you have both the 
encryption keys and the plain text. (in this case just enter 19 when promted
for the key...)

*****************************************************************************
* Question 3                                                                *
*****************************************************************************
3) Callig function Question3() will print out the answer for the question 3.

*****************************************************************************
* Question 4                                                                *
*****************************************************************************
4) Calling function Question4() will print out the answer for the question 4.

*****************************************************************************
* Question 5                                                                *
*****************************************************************************
 5) Given the function the cipher text and the key vector (cipher text has to 
 be just letters and no empty spaces or punctuation marks) prints the 
 decrypted plain text. (just run it with given params and it will print)

*****************************************************************************
* Question 6 (BONUS)                                                        *
*****************************************************************************
6) Given a cipher text as text file named "bonus_var.txt", it uses statistical
probability by shifting and comparing the cipher text with its right shifted 
versions, this function finds most likely top 3 key vector lenghts and pics
the most likely one. Then calculates the cipher text statistics for the 
distinct sub-ciphers as many as key vector lenght and prints top 4 candidates
for each sub-cipher. Then it calculates the probability of each of these 4 
candidates from each sub-cipher for being shifted from E and calculates the
likelihood of that scenario using the english letters' statistics. The 
scenario with highest likelihood is the most possible scenario so from each
sub-cipher the highest scenarioed vec key components are picked and used 
to decrypt the cipher text. Function can be easily modified to try top 
5 possible key lenghts and many more trials of alphabetical statistics other 
than E but since with only E it was able to solve it, I didnt implement those
parts but as I have coded everything to be mostly generic and modular it is
very easy to implement if needed. Just call the function and it will print all
necessary steps and informations.