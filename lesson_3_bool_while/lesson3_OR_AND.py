# AND   TRUE    FALSE
# TRUE
# False


print("AND bool tables")

operator = 'AND'
print(f'{operator}', "True", "False", sep=" " * 4)
print("True", True and True, True and False, sep='\t')
print('False', False and True, False and False, sep='\t')

operator = 'OR'
print(f'{operator}', "True", "False", sep=" " * 4)
print("True", int(True and True), '\t', f' {int(True and False)}', sep='\t')
print('False', int(False and True), '\t', f' {int(False and False)}', sep='\t')

