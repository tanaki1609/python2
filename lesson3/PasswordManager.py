"""
Write a class called Password_manager. The class should have a list called old_passwords
that holds all of the user’s past passwords. The last item of the list is the user’s current password. There should be a method called get_password that returns the current password
and a method called set_password that sets the user’s password. The set_password
method should only change the password if the attempted password is different from all
the user’s past passwords. Finally, create a method called is_correct that receives a string
and returns a boolean True or False depending on whether the string is equal to the current
password or not.
"""


class PasswordManager:
    old_passwords = ['asdfasd', '1232134123', 'asdfg']

    def set_password(self, password):
        self.old_passwords.append(password)

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password):
        pass

manager = PasswordManager()
manager.set_password(password=input('Enter a password: '))
print(manager.get_password())