from invmodn import invmodn
def exp_func(x, y):
    exp = bin(abs(y))
    print(len(exp))
    value = x
    negative = 0
    if(y==0): return 1
    if(y<0): negative = 1
 
    for i in range(3, len(exp)):
        value = value * value
        print("operation ",i)
        if(exp[i:i+1]=='1'):
            value = value*x
            print("operation x",i)
    

    if(negative == 1) : return (1/value)

    return value
#res = exp_func(2,1025)
#print(res)

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
    

    if(negative == 1) : return (invmodn(n,value))

    return value

#res = my_power_mod(2,1025,120)
#print(res)