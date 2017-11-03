
def fact(n):
  if n == 1:
    return 1
  else:
    return n*fact(n-1)
print(fact(4))

def fib(x):
    #assumes x is a int greater than 0
    #retuns the Fibonacci of x
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(15))



