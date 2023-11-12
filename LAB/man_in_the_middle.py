from EC_point_add import EC_exponent

G = [7,14]

a = 9
p = 17

Bob_b = 3
Bob_key = EC_exponent(a,p,Bob_b,G) # from Bob to MITM
MITM_b = 4
MITM_key = EC_exponent(a,p,MITM_b,G) # from MITM to Alice

Alice_a = 2
Alice_key = EC_exponent(a,p,Alice_a,G) # from Alice to MITM
MITM_a = 3
MITM_key = EC_exponent(a,p,MITM_a,G) # from MITM to Bob

# key sheared between Bob and MITM
Bob_MITM_key = EC_exponent(a,p,MITM_a,Bob_key)
print("Bob_MITM_key : ",Bob_MITM_key)
# key sheared between Alice and MITM
Alice_MITM_key = EC_exponent(a,p,MITM_b,Alice_key)
print("Alice_MITM_key : ",Alice_MITM_key)




