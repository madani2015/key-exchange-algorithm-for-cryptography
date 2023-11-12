

print("#=====================================invmodn============================================#")

def my_gcd(x , y):
    if y == 0:
        return x
    else:
        return my_gcd(y, x % y)

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)


def invmodn(N, a):
    if my_gcd(N, a) == 1:
        gcd,x, y = extended_euclidean(N, a)
        #print(f"{x}*{N}+{y}*{a}={gcd}")
        if(y<0) : y = y+N
        print(f"the inverse of {a} mod {N} = {y}")
        return y
    else:
        print("we cannot generate the inverse because the gcd is different than one")


#invmodn(N = 15,a =5 )
