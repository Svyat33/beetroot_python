string = 'my'
string_length = len(string)
string_last_chars = string_length - 2

if string_length >= 2:
    print(f'{string[:2]}{string[string_last_chars:]}')
else:
    print('Empty string')

