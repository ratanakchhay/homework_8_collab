def remove_all_after(numbers, n):
#create a new list to store the result
#if the number is greater than n, stop adding to the result
#if the number is equal to n, break the loop
# return the result list 
    result = []
    for i in numbers:
        result.append(i)
        if i == n:
            break
    return result
#take input from the user and make it to the list
numbers_input = input("Enter a list of numbers separated by spaces (ex:1 2 3): ")
numbers = [int(x) for x in numbers_input.split()]
n = int(input("Enter a boarder element: "))
print(f'The result is: {remove_all_after(numbers, n)}')