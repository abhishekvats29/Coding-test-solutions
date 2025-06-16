def generate_custom_odd_series(a):
    # If 'a' is even, reduce by 1 to get the previous odd number
    if a % 2 == 0:
        a -= 1

    result = []
    for i in range(1, a + 1, 2):
        result.append(i)
    
    print(", ".join(map(str, result)))

# Example usage
a = int(input("Enter a number: "))
generate_custom_odd_series(a)
