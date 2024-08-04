from itertools import permutations

# Permutate the digits used to form the date
# Normally O(n!) but since the input is fixed at 8 digits, it's fast enough
def permutateMMDDYYYY(date):
    digits = [digit for digit in date]
    unique_permutations = set(permutations(digits))

    result = []
    for perm in unique_permutations:
        result.append(''.join(map(str, perm)))

    return result

# Check if the given year is a leap year
def leapYear(year):
    year = int(''.join(map(str, year)))
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

# Check if a date permutation is a valid calendar date
def isValidDate(MMDDYYYY):
    # List of integers easier to work with. I guess you could also use modulo 10, but this is more readable
    date_list = [int(i) for i in str(MMDDYYYY) if i.isdigit()]

    month = date_list[0] * 10 + date_list[1]
    if month > 12 or month == 0: # Impossible month
        return False
    
    days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    date = date_list[2] * 10 + date_list[3]

    if date == 0 or date > 31: # Impossible date
        return False

    if month == 2: # February special case
        if leapYear(date_list[4:]):
            if date > 29:
                return False
        else:
            if date > 28:
                return False
    elif date > days[month]: # Invalid date
        return False
        
    return True # Good to go

# Compare two dates in chronological order True if `date1` is earlier than `date2`
def compare_dates(date1, date2):
    date1_list = [int(i) for i in str(date1) if i.isdigit()]
    date2_list = [int(i) for i in str(date2) if i.isdigit()]
    month1, day1, year1 = date1_list[:2] , date1_list[2:4], date1_list[4:]
    month2, day2, year2 = date2_list[:2] , date2_list[2:4], date2_list[4:]

    if year1 < year2: # See if year can settle it
        return True
    elif year1 == year2:
        if month1 < month2: # See if month can settle it
            return True
        elif month1 == month2:
            if day1 < day2: # See if day can settle it
                return True
            
    return False

N = int(input()) # Number of test cases
for _ in range(N):
    data = input()
    digits = [] # Gather digits to work with
    for i in range(len(data)):
        if data[i].isdigit():
            digits.append(int(data[i]))

    at_least_one = False
    earliest_date = 12319999 # Latest possible date
    
    perms = permutateMMDDYYYY(digits) # All permutations of the digits, regardless of validity for now

    count = 0 # Count for valid dates, which must be after Jan 1st, 2000 as per the problem statement
    for perm in perms:
        if len(str(perm)) != 8:
            continue

        fifth_digit = int(list(str(perm))[4]) # Equivalently, the first digit of the year
        if fifth_digit <= 1: # If year is 2000 or later, it satisfies validity
            continue

        if isValidDate(perm): # If valid date is also a valid calendar date,
            # update the variables
            if compare_dates(perm, earliest_date):
                earliest_date = perm
            at_least_one = True
            count += 1

    # Print results
    if not at_least_one:
        print("0")
    else:
        print(count, end=" ")
        earliest_date = str(earliest_date)
        print(earliest_date[2:4], earliest_date[:2], earliest_date[4:])
