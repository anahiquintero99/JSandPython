
def binary_array_to_number():
    arr = [1, 1, 1, 1, 0, 0, 0, 1, 0]
    arr.reverse()
    result = 0
    for indice in range(0, len(arr)):
        value = arr[indice] * pow(2, indice)
        result = result + value
    print(arr)
    print(result)


binary_array_to_number()
