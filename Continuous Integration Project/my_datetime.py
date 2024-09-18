def my_datetime(num_sec):
    """Convert seconds since epoch to a formatted date string."""

    # Check if a year is a leap year
    def is_leap_year(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    # Calculate the year based on the number of seconds
    SECONDS_IN_DAY = 86400
    DAYS_IN_YEAR = 365
    year = 1970

    while num_sec >= SECONDS_IN_DAY * (DAYS_IN_YEAR + is_leap_year(year)):
        num_sec -= SECONDS_IN_DAY * (DAYS_IN_YEAR + is_leap_year(year))
        year += 1

    # Calculate the month and day based on the numbver of seconds and year
    MONTHS = [
        ("January", 31),
        ("February", 28 + is_leap_year(year)),
        ("March", 31),
        ("April", 30),
        ("May", 31),
        ("June", 30),
        ("July", 31),
        ("August", 31),
        ("September", 30),
        ("October", 31),
        ("November", 30),
        ("December", 31),
    ]

    for month_name, days in MONTHS:
        if num_sec < days * SECONDS_IN_DAY:
            day = num_sec // SECONDS_IN_DAY + 1
            break
        num_sec -= days * SECONDS_IN_DAY

    # Convert month name to month number
    MONTH_NUMBERS = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    # Format the date string
    formatted_date = f"{MONTH_NUMBERS[month_name]:02}-{day:02}-{year}"
    print(formatted_date)
    return formatted_date
