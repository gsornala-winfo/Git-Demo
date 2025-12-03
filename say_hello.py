#v1.1.5
import bcrypt

def passwordHash():
    # Hashing a password
    password = b"MyStrongPassword"
    salt = bcrypt.gensalt()
    print(salt)
    hashed = bcrypt.hashpw(password, salt)
    return hashed

# Verification
user_input = b"MyStrongPassword"
hashed = passwordHash(user_input)
print(f'Hashed: {hashed}')
if bcrypt.checkpw(user_input, hashed):
    print("Password matches.")
else:
    print("Incorrect password.")
    print("Test line")

