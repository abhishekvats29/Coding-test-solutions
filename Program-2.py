def generate_odd_series(a):
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    print(", ".join(map(str, result)))

# Example usage
a = int(input("Enter a number: "))
generate_odd_series(a)
