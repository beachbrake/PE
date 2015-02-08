# Largest prime factor of the number 600851475143

a = 2
n = 600851475143
while a < n:
    if n % a == 0:
        n /= a
    else:
        a+= 1
print n
