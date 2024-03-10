from flask import flash

class InputValidation():
    def check_len_basics(self, request):
        
        self.email = request.form.get('email')
        self.firstName = request.form.get('firstName') 
        self.password1 = request.form.get('password1')
        self.password2 = request.form.get('password2')

        if len(self.email) < 7 or len(self.firstName) < 4 or len(self.password1) < 8:

            flash(f"Email must be greater than 4 characteres, " \
                   "First Name must be greater than 4 characteres and " 
                   "Password must be grater than 8 characteres", category='error')


    def signup_match_passwords(self, request):
        if self.password1 != self.password2: 
           flash("Passwords dont match", category='error')
    
