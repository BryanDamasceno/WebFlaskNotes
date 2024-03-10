from flask import Blueprint, render_template, request, flash
from website.security.input_checks import InputValidation

auth = Blueprint('auth', __name__)
validate_input = InputValidation()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", user="bryan") 


@auth.route('/logout')
def logout():
    return "<p>logout</p>"



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':                
        validate_input.check_len_basics(request)
        validate_input.signup_match_passwords(request)
 
    flash('Account created!', category='success')
    return render_template("signup.html", user="bryan")





