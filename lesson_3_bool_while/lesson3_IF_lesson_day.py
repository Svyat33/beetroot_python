day = 'Wednesday'


def if_lessons_today(day):
    if day == 'Tuesday' or day == 'Thursday':
        return True
    else:
        return False


print(if_lessons_today(day))
