from my_gcd import my_gcd

print("#=====================================Euler totient============================================#")

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def euler_totient(n):
    cop_numbers = []
    if (isPrime(n)):
        print(f"{n} is prime. The Euler's totient function is equal to {n-1}")
        return n-1

    for i in range(1, n):
        if my_gcd(i, n) == 1:
            cop_numbers.append(i)
    print(f"the coprime numbers of {n} are {cop_numbers}")
    totient = len(cop_numbers)
    print(f"the Euler's totient function is equal to {totient}")
    return totient


#euler_totient(2798)
print("================================================================")

def prime_factors(n):  
    prime_factors_list= []
    # Using the while loop, we will print the number of two's that divide n  
    while n % 2 == 0:
        if 2 not in prime_factors_list:
            prime_factors_list.append(2)  
          
        n = n / 2  
  
    for i in range(3, int(n**0.5) + 1, 2):  
  
        # while i divides n , print i ad divide n  
        while n % i == 0:  
            if i not in prime_factors_list:
                prime_factors_list.append(i)  
            n = n / i  
    if n > 2:  
        if i not in prime_factors_list:
                prime_factors_list.append(n) 
     
    return prime_factors_list

#print(prime_factors(2491))  
    
def special_euler_totient(n):
    # this part calculates the unique prime factors of the number n
    prime_factors_list = prime_factors(n)
    
    print(f"prime factors of {n} are {prime_factors_list}")
    totient = 1
    for i in prime_factors_list:
        totient = totient * (1 - 1 / i)
    totient = totient * n
    print(f"the Euler's totient function is equal to {int(totient)}")
    return int(totient)


#special_euler_totient(90)

print("================================================================")

