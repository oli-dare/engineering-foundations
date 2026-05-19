#print formatted logs

username = "admin_user"
user_id = 1042
balance = 1500.75
is_active = True

# My implementation here
print("Hello,", username)
print(f"ID: {user_id}")
print(f"{balance:.2f}")
print(is_active, "Seperate", sep="-", end=" | ")
print("Statement")
