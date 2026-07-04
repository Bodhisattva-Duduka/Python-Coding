# Check that a tuple type cannot be changed in python.
Tuple = (23, 34 , 564.34, 75.64, "apple")
Tuple[0] = 53
print(Tuple)
# Hence we cannot change tuple type