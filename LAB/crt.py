def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def crt(r_array,p_array):
    if (len(r_array) != len(p_array)):
        print("r and p MUST have the same size")
        
    else:
        sum = 0
        prod = 1
        for i in p_array:
            prod = prod * i
        for p_i, r_i in zip(p_array, r_array):
            p = prod // p_i
            sum += r_i *extended_euclidean(p_i,p)[2] * p
        return sum % prod,prod

r_array =[9,12,17]
p_array =[17,19,23]

print("the solution is: x = ",crt(r_array,p_array)[0]," mod ",crt(r_array,p_array)[1])

