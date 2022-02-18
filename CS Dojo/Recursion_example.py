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

      
