

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def EC_point_add(p,P,Q):
    if(P[0] == Q[0]) : return "c'est l'infini"
    r=[0,0]
    s=(P[1]-Q[1]) * extended_euclidean(p,P[0]-Q[0])[2] % p
    y0 = (P[1] - s * P[0]) % p
    r[0] = (s*s - P[0] - Q[0]) % p
    r[1] = -(y0 + s*r[0]) % p
    return r

def EC_point_double(a,p,P):
    r=[0,0]
    if(P[1] == 0) : return "c'est l'infini"
    s=(3 * P[0]*P[0] + a) * extended_euclidean(p,2 * P[1])[2] % p

    y0 = (P[1] - s * P[0])%p
    
    r[0] = (s*s - 2 *P[0]) % p
    r[1] = -(y0 + s*r[0]) % p
    return r

#print(EC_point_double(1,11,[2,4]))

#print(EC_point_add(11,[5,9],[2,4]))


def EC_exponent(a,p,k,P):
    exp = bin(abs(k))
    value = P

    for i in range(3, len(exp)):
        value = EC_point_double(a,p,value)
        if(exp[i:i+1]=='1'):
            value = EC_point_add(p,value,P)

    return value  
# for i in range(14):
#     print(f'**** {EC_exponent(1,11,i,[2,4])} , i = {i} ********')

def ECDH(a,p,G):
    # fixer les parametres
    expAlice = 2
    expBob = 4
    Qa = EC_exponent(a, p,expAlice, G)
    Qb = EC_exponent(a, p, expBob, G)
    Sa = EC_exponent(a, p, expAlice, Qb)
    Sb = EC_exponent(a, p, expBob, Qa)
    return Qa,Qb,Sa,Sb
print(ECDH(1,11,[3,5]))

    
         
            
    
g = [2, 4]
a = 29
b = 11;
p = 17;
