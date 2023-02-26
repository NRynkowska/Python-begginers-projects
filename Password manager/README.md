# Password manager
To use this program you need to install ```cryptography``` library. This library contains Fernet which is responsible for encrypting and decrypting passwords using generated key.

To generate key you need to uncomment following code: 
```python3
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
```
Passwords are stored in password.txt file in encrypted version.

