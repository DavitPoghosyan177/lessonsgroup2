def my_fib(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return my_fib(n-1) + my_fib(n-2)
 
print(my_fib(7))