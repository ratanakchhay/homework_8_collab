def reverse_ascending(numbers):
    if type(numbers) == list:
        if len(numbers) == 0:
            return numbers
        
        numbers.sort()
        return numbers[::-1]
    else:
        return "Not a List"
    
'''UI'''
msg = '''
Welcome to the Reverse Ascending List!
==========================================
Instructions:
    1. Input the amount of elements.
    2. Input the elements one by one.
    3. You will receive an ascending list.
'''
def intInput():
    try:
        intInput = int(input('Enter the data: '))
    except:
        return 0
    else:
        return intInput

def main():
    print(msg)

    list_of_data = []

    try: 
        number_of_elements = int(input("Enter the number of data: "))
    except:
        print("\n*100")
        main()
    else:
        for i in range(number_of_elements):
            list_of_data.append(intInput())
    
    print("The result is: ",reverse_ascending())
    