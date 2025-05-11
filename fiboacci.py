def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
terms = int(input("Enter the number of terms: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    print(fibonacci_series(terms))
