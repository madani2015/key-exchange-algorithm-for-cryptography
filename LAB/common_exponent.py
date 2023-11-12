from crt import crt
def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def common_exponent(Ei,Ri,k):
    for i in range(len(Ri)):
        for j in range(i+1,len(Ri)):
            if(extended_euclidean(Ri[i],Ri[j])[0] != 1):
                return "Hypotesys non respected"
    x = crt(Ei,Ri)[0]
    m = round(x ** (1/k))
    if(m > min(Ri)) : return "Hypotesys non respected"
    return round(x ** (1/k))

print("plaintext is : ",common_exponent([9,12,17],[17,19,23],3))

# 9 = 15 ** 3 % 17
# 12 = 15 ** 3 % 19
# 17 = 15 ** 3 % 23