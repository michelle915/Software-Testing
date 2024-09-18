# dictionary for integers
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
    """
    This function takes in a string and converts  it into a base 10 number, and returns it.
    It has the following specifications:
    Must be able to handle strings that represent integers
    Must be able to handle strings that represent floating-point numbers
    Must be able to handle hexadecimal numbers with the prefix 0x
    Must be case-insensitive
        Negative numbers are indicated with a - like -0xFF
        Only integers are valid inputs for hexadecimal numbers (i.e., no 0xFF.02)
        The type returned must match the type sent.
    Invalid formats should return None, including, but not limited to:
        strings with multiple decimal points
        strings with alpha that aren't part of a hexadecimal number
        strings with a hexadecimal number without the proceeding 0x
        values for num_str that are not strings or are empty strings
    """
    # return None immediately if input is not a string or empty
    if isinstance(num_str, str) is False or num_str == '':
        return None
    # categorize initial inputs
    input_category = process_inputs(num_str)
    if input_category.get("decimal_count") > 1:
        return None
    # check all characters are valid
    if validate_num_str(num_str, input_category["negative"], input_category["hex"]) == "error":
        return None
    # convert to number
    return_result = convert_num_str(num_str, input_category["negative"], input_category["hex"],
                                    input_category["decimal_count"], input_category["decimal_pos"])
    # round decimal and ensure there is a zero after the decimal point
    if input_category["decimal_count"] == 1:
        return_result = return_result + 0.0
        return_result = round(return_result, 1 + (len(num_str) - input_category["decimal_pos"]))
    return return_result


def process_inputs(num_str):
    """
    Process initial inputs into useful categories
    """
    process_dict = {
        "negative": 0,
        "decimal_count": 0,
        "decimal_pos": 0,
        "hex": 0
    }
    if num_str[0] == '-':
        process_dict["negative"] = 1
    if num_str[0:2] == "0x" or num_str[0:3] == "-0x":
        process_dict["hex"] = 2
    process_dict["decimal_count"] = num_str.count('.')
    process_dict["decimal_pos"] = num_str.find('.')
    return process_dict


def validate_num_str(num_str, is_negative, is_hex):
    """
    Check that all characters are valid based on the type of input
    """
    slice_header = is_negative + is_hex
    validate_dict = numdict
    num_str = num_str[slice_header:]
    if is_hex == 2:
        validate_dict = hexdict
    for char in num_str:
        if char.lower() not in validate_dict:
            return "error"


def convert_num_str(convert_str, is_negative, is_hex, is_decimal, decimal_pos):
    """
    Convert num_str to a numeral format
    """
    # process num_str
    processed_str = convert_str.replace('.', '').replace('-', '')
    processed_str = processed_str[is_hex:]
    convert_length = len(processed_str)
    # conversion constants
    convert_dict = numdict
    convert_factor = 10
    if is_hex == 2:
        convert_dict = hexdict
        convert_factor = 16
    convert_start = convert_length
    if is_decimal == 1:
        convert_start = decimal_pos - is_negative
    # convert to correct number format
    convert_result = 0
    for num in range(convert_length):
        convert_result = convert_result + convert_dict[processed_str[num].lower()] \
                         * convert_factor ** (convert_start - num - 1)
    if is_negative == 1:
        convert_result = convert_result * -1

    return convert_result


def my_datetime(num_sec):
    """Convert seconds since epoch to a formatted date string."""

    # Check if a year is a leap year
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # Calculate the year based on the number of seconds
    SECONDS_IN_DAY = 86400
    DAYS_IN_YEAR = 365
    year = 1970

    while num_sec >= SECONDS_IN_DAY * (DAYS_IN_YEAR + is_leap_year(year)):
        num_sec -= SECONDS_IN_DAY * (DAYS_IN_YEAR + is_leap_year(year))
        year += 1

    # Calculate the month and day based on the numbver of seconds and year
    DAYS_IN_MONTH = [
        31,  # January
        28,  # February
        31,  # March
        30,  # April
        31,  # May
        30,  # June
        31,  # July
        31,  # August
        30,  # September
        31,  # October
        30,  # November
        31,  # December
    ]

    # Update February if it is a leap year
    if is_leap_year(year):
        DAYS_IN_MONTH[1] = 29

    # Calculate the month and day based on the number of seconds and year
    month = 0
    while num_sec >= DAYS_IN_MONTH[month] * SECONDS_IN_DAY:
        num_sec -= DAYS_IN_MONTH[month] * SECONDS_IN_DAY
        month += 1

    day = num_sec // SECONDS_IN_DAY + 1
    month += 1

    # Format the date string
    formatted_date = f"{month:02}-{day:02}-{year}"
    return formatted_date


def conv_endian(num, endian='big'):
    """
    This function takes in an integer value as num and converts it to a hexadecimal number.
    The endian type is determined by the flag endian. The function will return the converted
    number as a string. It has the following specifications:
        - assumed that num will always be an integer
        - handles negative values for num
        - value of big for endian will return a hexadecimal number that is big-endian
        - value of little for endian will return a hexadecimal number that is little-endian
        - any other values of endian will return None
        - the returned string will have each byte separated by a space
        - each byte is two characters in length
    """
    # Validate endian input
    if endian not in ['big', 'little']:
        return None

    # Handle input of 0
    if num == 0:
        return '00'

    # Handle the sign
    if num < 0:
        sign = '-'
        num = -num
    else:
        sign = ''

    # Helper function to convert integer to hexadecimal
    def int_to_hex(n):
        hex_dict = {
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
        }

        hex_result = []

        # Append hexadecimal digits to hex_result in least-significant to most-significant order
        while n > 0:
            hex_result.append(hex_dict[n % 16])
            n //= 16

        # If the length of hex_result is odd, append with '0' so each byte will be two characters
        if len(hex_result) % 2 != 0:
            hex_result.append('0')

        # Reverse hex_result into conventional most-sig to least-sig order & concatenate result into str
        return ''.join(reversed(hex_result))

    hex_value = int_to_hex(num)

    # Split into bytes and pad each byte to be 2 characters (ex: ['ABCD'] -> ['AB', 'CD'])
    hex_bytes = [hex_value[i:i + 2] for i in range(0, len(hex_value), 2)]

    # Reverse bytes for little-endian representation (ex: ['AB', 'CD'] -> ['CD', 'AB'])
    if endian == 'little':
        hex_bytes = reversed(hex_bytes)

    # Return hex conversion with one space between each bite
    return sign + ' '.join(hex_bytes)
