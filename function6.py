# list all elements add, we are pass parameters as a list.
def add_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

total_result = add_numbers([12, 34, 45, 67, 45, 56, 66])
print(total_result)
