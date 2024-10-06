def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def fib(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, (a + b) % mod
        return b

def main(a, b, M):
    fib_a = fib(a, M)
    fib_b = fib(b, M)
    g = gcd(fib_a, fib_b)
    result = g % M
    return result

if __name__ == "__main__":
    a = 10
    b = 15
    M = 1000000007
    result = main(a, b, M)
    print(f"{result}")