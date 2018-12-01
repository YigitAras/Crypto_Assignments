#! /home/yigitaras/anaconda3/envs/cryptoenv/bin/python3
# Do not forget to install pycryptodome if not laready installed
# pip install pycryptodome

import random

from Crypto.Hash import SHA256
hash = SHA256.new()
hash.update(b'message')
print (hash.digest())
print (hash.hexdigest())
hash_int = int.from_bytes(hash.digest(), byteorder='big')

# The last number in the following message is a nonce
message = b'Donald Trump has just sent 1000 Satoshi to Erkay Savas - 5678123790' 
hash = SHA256.new(message)
digest = hash.hexdigest()
print ("\nmessage:", message)
print ("digest: ", digest)

# second message with a hash whose prefix (one or more hexadecimal characters) is matching with the first message
# This example illustrates how hard it is to find collisions in a cryptographic hash function
match_count = 5
message_ = b'Donald Trump has just sent 1000 Satoshi to Erkay Savas - '
start = random.randint(0,2**30)
i = start
while True:
  hash_ = SHA256.new(message_ + str(i).encode('utf-8'))
  digest_ = hash_.hexdigest()
  if (digest[0:match_count] == digest_[0:match_count]):
    print("message_: ", message_ + str(i).encode('utf-8'))
    print("digest_: ", digest_)
    break
  i = i+1  

print("number of trials", i-start)

print("\nExercise 02: ")
print("We will be simulating Proof-of-Work in bitcoin")
print("Consider the message: ", b'Donald Trump has just sent 1000 Satoshi to Erkay Savas - ')
print("By adding a random nonce at the end of the message, your mission is to find a hash value that is smaller than ")
print("2**236")
print("print the hash value in hexadecimal format")


for i in range(0,2**236):
  hash__ = SHA256.new(message_ + str(i).encode('utf-8'))
  digest__ = hash__.hexdigest()
  if 2**236 > (int.from_bytes(hash__.digest(), byteorder='big')):
      print("digest__: ",digest__)
      break
print("Trials required: ", i)
