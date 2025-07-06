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