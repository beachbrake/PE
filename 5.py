# Smallest positive number fully divisible by all numbers from 1 to 20
# Also means that the number is even, as hidden in the question is divible by 2

x = 2
while True:
    divisible = True
    for i in range(2,21):
        if x % i != 0:
            divisible = False
            break
    if divisible:
        break
    x += 2

print x
