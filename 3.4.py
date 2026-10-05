import string
# exceptions
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, character, index):
        self.character = character
        self.index = index
    def __str__(self):
        return "The username contains an illegal character: " + self.character + " at index " + str(self.index)

class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"

class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"

class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"

class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"

class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"





def check_input(username, password):

    # Username too short
    if len(username) < 3:
        raise UsernameTooShort()

    # Username too long
    if len(username) > 16:
        raise UsernameTooLong()
    # Username haas illegal character
    for i in range(len(username)):
        if not (username[i].isalpha() and username[i].isascii()) and not username[i].isdigit() and username[i] != "_":
            raise UsernameContainsIllegalCharacter(username[i], i)
    #  too short
    if len(password) < 8:
        raise PasswordTooShort()
    #  too long
    if len(password) > 40:
        raise PasswordTooLong()

    #  missing uppercase
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()

    #  missing lowercase
    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase()

    #  missing digit
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()
    #  missing special character
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()
    print("OK")


def main():
   # check_input("A_1", "abcdefghijklmnop")
    #check_input("A_1", "ABCDEFGHIJLKMNOP")
    #check_input("A_1", "ABCDEFGhijklmnop")
   # check_input("A_1", "4BCD3F6h1jk1mn0p")
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            check_input(username, password)
            break

        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()