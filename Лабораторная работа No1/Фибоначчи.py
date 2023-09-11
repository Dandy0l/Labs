def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        if n == b:
          return True
    return False

print(fib(4))
print(fib(2))
print(fib(22))
print(fib(5))
print(fib(3))