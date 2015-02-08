#Find the sum of all the multiples of 3 or 5 below 1000
a = 0
sum = 0
while a < 1000:
    if a % 3 == 0 or a % 5 == 0:
        sum += a
    a += 1
print sum
