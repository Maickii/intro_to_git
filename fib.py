def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

num_terms = 20
fib_sequence = fionacci(num_terms)
print("Fibonacci sequence:", fib_seuence)
