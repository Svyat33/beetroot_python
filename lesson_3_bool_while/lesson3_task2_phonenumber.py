phone_number = '0123456789'
# Если делать исполняемый файл или вводить phone_number через терминал,
# возможно, значение будет приведено к integer, по этому сделал доп приведение к string
phone_number = str(phone_number)
phone_number_length = len(phone_number)

if phone_number.isdigit() and phone_number_length == 10:
    print('You entered next phone number: %s' % phone_number)
elif phone_number_length != 10 and not phone_number.isdigit():
    print('Using letters and whitespaces is not allowed and number must contain only 10 digit\'s.')
elif phone_number_length != 10:
    print('Phone number must contain only 10 digit\'s and have the following format: 0123456789')
elif not phone_number.isdigit():
    print('Phone number must contain only digit\'s. Using letters, whitespaces and other symbols is not allowed.')
else:
    print('Something else going wrong')
