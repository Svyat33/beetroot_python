from datetime import datetime

name = 'Roman'
date_current = datetime.now()
day = date_current.strftime("%A")

# Good day Roman!  Monday is a perfect day to learn some python.
print(f'Good day {name}! ', '%s is a perfect day to learn some python.' % day)



