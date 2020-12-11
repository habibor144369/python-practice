#Average diagnosis
def add_numbers(numbers_list):
    count = 0
    for numbers in numbers_list:
        count += numbers
    return count

list_item = [34, 787, 43, 56, 75, 37, 67]
total_result = add_numbers(list_item)
print(total_result)
