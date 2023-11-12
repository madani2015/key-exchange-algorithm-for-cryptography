print("#=====================================gcd============================================#")


def my_gcd(a, b):
    string = f"gcd({a},{b})="
    r = a % b
    while r > 0:
        r = a % b
        a = b
        b = r
    print(string, a)
    return a


#my_gcd(35, 15)


