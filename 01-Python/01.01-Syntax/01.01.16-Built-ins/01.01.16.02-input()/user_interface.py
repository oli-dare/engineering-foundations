# process user input

name = input("Name: ")
age = int(input("Age: "))
tax_rate = float(input("Tax Rate: "))

birth_year = 2026 - age
print(f"Name: {name} | Tax rate: {tax_rate:.1f} | birth year: {birth_year}")