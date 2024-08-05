def calculate_statistics(numbers):
    if not numbers:
        return None, None

    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

    return mean, variance


numbers = [1, 2, 3, 4, 5]
mean, variance = calculate_statistics(numbers)
print(f"Mean: {mean}, Variance: {variance}")
