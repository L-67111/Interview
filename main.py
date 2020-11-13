
"""
Its length is at least 6
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: `!@#$%^&*()-+`

request user to enter a password (nothing entered exception)
user enters string
check for criteria above

req 2:
parse each character in the string
test if any or at least 1 is a integer


"""

password = input('Please enter your password')

#check length
def enter_password(password):
    if len(password) < 6:

        return False
    else:
        return True

#check for digit
def check_digit(password):
    for i in password:
        if i.isdigit():
            return True
    return False









print(enter_password(password))
