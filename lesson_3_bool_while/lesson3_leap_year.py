year_for_test = 2020


'''def is_leap_year(year):
    reminder_for_4 = year % 4
    # if not reminder => reminder False => not reminder than leap year
    return not reminder_for_4 or False # not reminder == 0 == True
    # if not reminder_for_4:
    #     return True
    # else:
    #     return False
'''
is_leap_year = not year_for_test % 4 or False

print(is_leap_year)
print(year_for_test % 4)

current_day = 'Sunday'

will_we_have_courses_today = current_day == 'Tuesday' or current_day == 'Thursday'
print(will_we_have_courses_today)
