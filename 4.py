# Largest palindrome made from the product of two 3 digit numbers

def palindrome(num):
    s = str(num)
    p = s[::-1]
    return p == s

largest = 0
product = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        product = a * b
        if palindrome(product):
            if largest < product:
                largest = product
    
print largest

