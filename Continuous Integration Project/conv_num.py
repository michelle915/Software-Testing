numdict = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
    ".": "decimal"
}

# dictionary for hex
hexdict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}


def conv_num(num_str):

    # initial check that input is string, otherwise too many tests below will fail
    if isinstance(num_str, str) is False:
        return None

    """
    categorize inputs
    """
    length = len(num_str)
    is_decimal = decimal_test(num_str, length)[0]
    is_negative = negative_test(num_str)
    is_hex = hex_test(num_str, is_decimal)
    decimal_pos = decimal_test(num_str, length)[1]
    decimal_count = decimal_test(num_str, length)[2]

    """
    validate input
    """
    test1 = validate_initial(length, decimal_count)
    if is_hex == 1:
        test2 = validate_hex(num_str, length, is_negative)
    else:
        test2 = validate_integer(num_str, length, is_negative)

    if (test1 + test2) > 0:
        return None

    """
    Call helper function to route to the correct solution function
    """
    result = router(is_hex, is_decimal, num_str, length, decimal_pos, is_negative)
    return result


def hex_test(num_str, is_negative):
    # determine if the input is a hex number
    is_hex = 0
    if is_negative == 0:
        if num_str[0:2].lower() == "0x":
            is_hex = 1
    else:
        if num_str[1:3].lower() == "0x":
            is_hex = 1
    return is_hex


def decimal_test(num_str, length):
    # find decimal if any and its position/count
    decimal_count = 0
    decimal_pos = 0
    is_decimal = 0

    if '.' in num_str:
        is_decimal = 1

    for num in range(length):
        if num_str[num] == '.':
            decimal_pos = num
            decimal_count += 1

    return [is_decimal, decimal_pos, decimal_count]


def validate_initial(length, decimal_count):
    # validate simple input conditions
    if length == 0:
        return 1
    if decimal_count > 1:
        return 1
    return 0


def validate_integer(num_str, length, is_negative):
    # make sure there are no invalid characters in an integer string
    int_pointer = 0 + is_negative
    for num in range(length):
        if num < int_pointer:
            continue
        if num_str[num] not in numdict:
            return 1
    return 0


def validate_hex(num_str, length, is_negative):
    hex_pointer = 2 + is_negative
    for num in range(length):
        if num < hex_pointer:
            continue
        if num_str[num].lower() not in hexdict:
            return 1
    return 0


def negative_test(num_str):
    # determine if the input is negative
    is_negative = 0
    if num_str[0] == "-":
        is_negative = 1
    return is_negative


def router(is_hex, is_decimal, num_str, length, decimal_pos, is_negative):
    if is_hex == 1:
        result = hex_conv(num_str, length, is_negative)
    elif is_hex == 0 and is_decimal == 1:
        result = int_float(num_str, length, decimal_pos, is_negative)
    elif is_hex == 0 and is_decimal == 0:
        result = int_conv(num_str, length, is_negative)
    else:
        result = "Unknown type, bug discovered"
    return result


def int_conv(num_str, length, is_negative):
    # convert string to INTEGER by multiplying each INTEGER by its position in the string
    int_result = 0
    int_pos = 0 + is_negative

    for num in range(length):
        if num < int_pos:
            continue
        int_result = int_result + ((numdict[num_str[num]]) * 10 ** (length - num - 1))

    if is_negative == 1:
        int_result = int_result * (-1)

    return int_result


def hex_conv(num_str, length, is_negative):
    # convert string to HEX by multiplying each HEX value by its position in the string
    hex_result = 0
    hex_pos = 2 + is_negative

    for num in range(length):
        if num < hex_pos:
            continue
        hex_result = hex_result + (hexdict[num_str[num].lower()]) * 16 ** (length - num - 1)

    if is_negative == 1:
        hex_result = hex_result * (-1)
    return hex_result


def int_float(num_str, length, decimal_pos, is_negative):
    # convert string to FLOAT by multiplying each FLOAT value by its position relative to the decimal position
    int_result = 0
    for num in range(length):
        if num_str[num] == '.' or num_str[num] == '-':
            continue
        if num - decimal_pos > 0:
            int_result = int_result + (numdict[num_str[num]]) * 10 ** (decimal_pos - num)
        if num - decimal_pos < 0:
            int_result = int_result + (numdict[num_str[num]]) * 10 ** (decimal_pos - num - 1)

    if is_negative == 1:
        int_result = int_result * (-1)

    # make sure the return result has 0 after the decimal before rounding
    int_result = int_result / 10 ** length * 10 ** length

    int_result = round(int_result, (length - decimal_pos))

    return int_result
