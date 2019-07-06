# find the greatest common denominator of two numbers using ECULID's algorithm

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % a

    return a

print(gcd(60, 96))
print(gcd(20, 8))
