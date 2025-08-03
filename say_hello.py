import bcrypt

# Hashing a password
password = b"MyStrongPassword"
salt = bcrypt.gensalt()
print(salt)
hashed = bcrypt.hashpw(password, salt)
print(hashed)

# Verification
user_input = b"MyStrongPassword"
if bcrypt.checkpw(user_input, hashed):
    print("Password matches.")
else:
    print("Incorrect password.")
