# Recursive function to calculate Fibonacci numbers
# def fibonacci_recursive(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
    
#     fib_sequence = fibonacci_recursive(n - 1)
#     fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence

# # Example usage
# n = int(input("Enter number of terms: "))
# print("Fibonacci sequence (Recursive):", fibonacci_recursive(n))





def finbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n==2:
        return 1
    
    return finbo(n-1) + finbo(n-2)


n = int(input())

print(finbo(n))