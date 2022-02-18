# N factorial:

def fact(n):
    if n>=1:
        return  n*fact(n-1)
    else:
        return 1
      
# Fibonacci Series

def fib(n):
    if n>=3:
        return  fib(n-1)+fib(n-2)
    else:
        return 1

      
# frog problem

def frog(n):
    if n>=1:
        return frog(n-1)+frog(n-2)
    else:
        return 1
      
def frog2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return  frog(n-1)+frog(n-2)

frog2(10)      
      
