from keygen import key_generator
from keygen import encryption
def my_power_mod(x,puissance,n):
    exp = bin(abs(puissance))
    value = x % n
    negative = 0
    if(puissance==0): return 1
    if(puissance<0): negative = 1
 
    for i in range(3, len(exp)):
        value = (value * value) % n
        if(exp[i:i+1]=='1'):
            value = (value*x) % n
    

    if(negative == 1) : return (extended_euclidean(n,value)[2])

    return value


def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)


def rsa_common_modulus_1(R,e1,e2,E1,E2):
    s1 = extended_euclidean(e2,e1)[2] # inverse modulo
    s2 = int((extended_euclidean(e1,e2)[0] -e1*s1)/e2)
    temp = extended_euclidean(R,E2)[2] # inverse modulo
    m1 = my_power_mod(E1,s1,R) 
    m2 = my_power_mod(temp,-s2,R)
    return (m1 * m2) % R

print("result :",rsa_common_modulus_1( R = 2491 , e1 = 3 , e2 = 15 , E1 = 680 , E2 = 364))
print("result :",rsa_common_modulus_1( R = 2491 , e1 = 3 , e2 = 5 , E1 = 680 , E2 = 1282))
 #test question 3
public_key,private_key = key_generator(17,13)
e1 = public_key[0]
print(e1)
public_key,private_key = key_generator(17,13)
e2 = public_key[0]
print(e2)
R = 17 * 23
E1 = encryption(254,e1,R)
E2 = encryption(254,e2,R)

print("result de test :",rsa_common_modulus_1( R , e1 , e2 , E1 , E2 ))



