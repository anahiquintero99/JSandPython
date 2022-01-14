
def binary_array_to_number():
    arr = [0, 0, 0, 1]
    arr.reverse()
    for indice in range(0, len(arr)):
        value = arr[indice] * pow(2, indice)
        suma = suma + value

    print(suma)


binary_array_to_number()
