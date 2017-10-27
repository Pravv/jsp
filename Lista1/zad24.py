def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
		
def zad24():
    n = 5
    for i in range(n):
        print(fib(i))
		
zad24()