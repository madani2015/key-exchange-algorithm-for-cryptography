import random
from invmodn import invmodn
from my_power import my_power_mod
from crt import crt
def my_gcd(a, b):
    string = f"gcd({a},{b})="
    r = a % b
    while r > 0:
        r = a % b
        a = b
        b = r
    print(string, a)
    return a


p = 13
q = 17 
def key_generator(p,q):
    phi_n = (p-1) * (q-1)
    n = p*q

    while True:
        i = random.randint(2,20)
        if(my_gcd(i,phi_n)==1):
            e=i
            
            break

    
    d = invmodn(phi_n,e)
    
    return [e,n],d

phi_n = (p-1) * (q-1)
n = p*q
public_key,private_key = key_generator(p,q)
e = public_key[0]
d = private_key

# print("e*d ",e*d % phi_n)

# print("public key (",e,", ",n,")")
# print("private key (d = ",d,")")


text = 15
ciphertext = []
plaintext = []
plaintext_crt = []
def encryption(P,e,n):
    return my_power_mod(P,e,n)

# print("******************encryption : ",encryption(125,5,13*17))

def decryption(C,d,n):
    return my_power_mod(C,d,n)

# print("**************decryption : ",decryption(177,77,13*17))

def decryption_crt(C,d,p,q):
    return crt([my_power_mod(C,(d%(p-1)),p),my_power_mod(C,(d%(q-1)),q)],[p,q])

# print("decryption crt: ",decryption_crt(177,77,13,17))

# for i in text:
#     ciphertext.append(encryption(i, e,n))
# print(f"***********ciphertext is : {ciphertext}")
# for i in ciphertext:
#     plaintext.append(decryption(i,d,n))
# print(f"***********plaintext is : {plaintext}")
# for i in ciphertext:
#     plaintext_crt.append(decryption_crt(i, d,p,q))
# print(f"***********plaintext is : {plaintext_crt}")

#If the message is very small, it can be retrieved by applying a cubic root on the ciphertext.
#decryption is faster : Why CRT is used to decrypt messages
