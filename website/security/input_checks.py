from flask import flash

class InputValidation():
    def check_len_basics(self,email, firstName, password1):
        if len(email) < 7 or len(firstName) < 4 or len(password1) < 8:

            flash(f"Email must be greater than 4 characteres, " \
                   "First Name must be greater than 4 characteres and " 
                   "Password must be grater than 8 characteres", category='error')


    def signup_match_passwords(self, password1, password2):
        if password1 != password2:
           flash("Password1 is different from Password2", category='error')
    
