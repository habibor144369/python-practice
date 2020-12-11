# multiplication table print by function---

def multiplication_table(table = 1):

    for number in range(1, 11):
        result = number * table
        print(number, 'x', result, '=', result)

multiplication_table(10)

