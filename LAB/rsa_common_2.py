from keygen import key_generator
from keygen import encryption
from euler_totient import prime_factors

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


def rsa_common_modulus_2(ea,da,eb,R):
    F = extended_euclidean(eb,da*ea-1)[0]
    C = int((da*ea - 1)/ F)
    gcd,_,db = extended_euclidean(C,eb)

    if(gcd != 1 ):
        C = 1 
        while extended_euclidean(C,eb)[0] != 1:
            C = C + 1
        db = extended_euclidean(C,eb)[2]
    #if db <0 or db > R : 
    #    return "resultat introuvable"
    
    return db

#print("result :",rsa_common_modulus_1( R = 2491 , e1 = 3 , e2 = 15 , E1 = 680 , E2 = 364))
#print("result :",rsa_common_modulus_1( R = 2491 , e1 = 3 , e2 = 5 , E1 = 680 , E2 = 1282))
R = 2491
factors= prime_factors(R)
public_key,private_key_a = key_generator(int(factors[0]),int(factors[1]))
e1 = public_key[0]
print(e1,private_key_a)
public_key,private_key_b = key_generator(int(factors[0]),int(factors[1]))
e2 = public_key[0]
print(e2,private_key_b)
# R = 2491
# E1 = encryption(254,e1,R)
# E2 = encryption(254,e2,R)

print("result de test :",rsa_common_modulus_2( e1 ,private_key_a, e2,R  ))



