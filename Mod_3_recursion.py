def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])
    #print(first)

    if first == 0:
        return 0

    elif len(str(str_number)) > 1:
        if get_multiplied_digits(int(str_number[1:])) == 0:
            return first
        else:
            return first * get_multiplied_digits(int(str_number[1:]))

    else:
        return first


result = get_multiplied_digits(40203)
print(result)

result_2 = get_multiplied_digits(402030)
print(result_2)