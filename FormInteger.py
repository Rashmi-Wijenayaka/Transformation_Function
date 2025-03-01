def form_integer(number):
    if number < 0:
        print ("Please provide a non-negative number.")
        return -1
    

    num_str = str(number)
    num_digits = len(num_str)
    last_digit = int(num_str[-1])
    result = num_digits * 10 + last_digit
    return result

number = int(input("Please provide a positive integer: "))
new_integer = form_integer(number)
if new_integer != -1:
    print ("The new integer is:", new_integer)