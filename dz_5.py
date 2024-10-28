def get_multiplied_digits(number):
    if type(number) == int:
        str_number = str(number)
        len_number = len(str_number)
        first = int(str_number[0])
        if len_number > 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first


result = get_multiplied_digits(40203)
print(result)
result_2 = get_multiplied_digits(23)
print(result_2)
