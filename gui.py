import bcrypt

password = b"ilovecomputers"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)