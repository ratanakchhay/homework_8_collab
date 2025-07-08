n = int(input("Choose the array index to put power: "))
array = [1, 2, 3, 4]

def index_power(array, n):
    if 0 <= n < len(array):
        result = array[n] ** 2
        print(result)
        return result
    else:
        return -1
    

index_power(array, n)