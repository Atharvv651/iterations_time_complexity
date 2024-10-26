def multiply_single_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b >= 0 else -result

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Result using single iteration:", multiply_single_iteration(x, y))
print("Result using n iterations:", multiply_n_iterations(x, y))
