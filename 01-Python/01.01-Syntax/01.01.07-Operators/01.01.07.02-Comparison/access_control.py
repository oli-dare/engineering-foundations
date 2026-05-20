user_role = "editor"
is_verified = False

#My implementation here
if user_role == "admin" and is_verified:
    print("Full Access")
elif user_role == "editor" and not is_verified:
    print("Pending Verification")
elif user_role == "guest" or not is_verified:
    print("Limited Access")
else:
    print("Access Denied")