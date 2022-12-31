import random
import string

letters = string.ascii_letters

def generate(length):
    password = "";
    for i in range(length):
        password += str(random.randint(0,9));
        password += random.choice(letters);
    return password;

firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
password_length = int(input("Please enter the length of your password: "));

print(f"{firstname} {lastname}")
print(f"Your password of length {password_length} is: {generate(password_length)} ");