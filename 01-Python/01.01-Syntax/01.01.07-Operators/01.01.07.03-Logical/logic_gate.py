#boolean logic evaluation

is_sunny = True
is_weekend = False
has_plans = False

# My implementation here
if is_sunny and is_weekend:
    print("Good Day")
elif is_sunny or (not is_weekend and has_plans):
    print("Should Go Out")
elif not is_weekend and not has_plans:
    print("Busy")