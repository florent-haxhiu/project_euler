# def fib(n):
#    if n == 1:
#       return 1
#    elif n == 0:   
#       return 0            
#    else:                      
#       return fib(n-1) + fib(n-2)

# print(fib(100))

def fib(n):
    return pow(2 << n, n + 1, (4 << 2*n) - (2 << n) - 1) % (2 << n)
  
print(fib(27))

add = 0

for i in range(50):
  if fib(i) < 4000000:
    if fib(i) % 2 == 0: add += fib(i)

print(add)