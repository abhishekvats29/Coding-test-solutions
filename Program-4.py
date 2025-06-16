def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

# Example usage
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(input_list)
print(output)
