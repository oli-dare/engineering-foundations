# complex type conversion

number = 10
text = "python"
sequence = [65, 66, 67]

# My implementation here
int_float = float(number)
int_bool = bool(number)
str_frozenset = frozenset(set(list(text)))
b = bytes(sequence)
b_array = bytearray(b)
b_array[0] += 1

print(int_float, int_bool, str_frozenset, b_array)