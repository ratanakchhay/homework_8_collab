def replace_last(numbers):
    """
    Moves the last element of a list to the first position.
    An empty list or a list with only one element remains unchanged.

    Examples:
    replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    replace_last([1]) == [1]
    replace_last([]) == []
    """
    if len(numbers) <= 1:
        return numbers
    else:
        last_element = numbers[-1]  # Get the last element
        # Create a new list with the last element first,
        # followed by all elements except the last one
        return [last_element] + numbers[:-1]

# Test cases:
print(f"replace_last([2, 3, 4, 1]) == {replace_last([2, 3, 4, 1])}")
print(f"replace_last([1, 2, 3, 4]) == {replace_last([1, 2, 3, 4])}")
print(f"replace_last([1]) == {replace_last([1])}")
print(f"replace_last([]) == {replace_last([])}")
