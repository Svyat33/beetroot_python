# Task 3
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

# for me: variable = [out_exp for out_exp in input_list if out_exp == 2]
# for me: что сделать с j для каждого j(которому присваиваются резуьтат за каждый проход) в range(1, 11)

print([tuple(range(1, 11),), tuple(j ** 2 for j in range(1, 11))])
