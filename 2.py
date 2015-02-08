# Find the sum of even valued terms of a Fibonacci sequence whose values do not exceed four million. The fibonacci starts with 1,2,3,5 ...

a = 1
b = 2
n = 0
fibsum = 2
while n < 4000000:
    n = a + b # 3 = 2 + 1
              # 5 = 3 + 2
              # 8 = 5 + 3
              # 13 = 8 + 5
    a = b
    b = n
        
    if n % 2 == 0:
        fibsum += n
    
print fibsum
        
    
