def repeat_count(array, inteiro):
    value = array.count(inteiro)
    return value


array = [1, 2, 3, 4, 5, 10, 5, 6, 5, 5, 5]
inteiro = 5
value = repeat_count(array, inteiro)
print(value)