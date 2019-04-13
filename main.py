from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
#write a function to get input from user
def gather_info():
    user_name = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
     
    error = ""
    if not(user_name):
        error = "You must complete this field."
        return render_template('sign-up-home.html', 
            username_error = error)
    if not(password):
        error = "You must complete this field."
        return render_template('sign-up-home.html', 
            password_error = error)
    if not(verify_password):
        error = "You must complete this field."
        return render_template('sign-up-home.html', 
            verify_password_error = error)
    
    if len(user_name) < 3 or len(user_name) > 20:
        error = user_name + " is not a valid username. Enter a username between 3-20 characters."
        return render_template('sign-up-home.html', username_error = error, username = user_name)

    if " " in user_name:
        error = "Usernames cannot contain spaces. Please try again."
        return render_template('sign-up-home.html', username_error = error, username = user_name)


    if len(password) < 3 or len(password) > 20:
        error = "Password is not a valid. Enter a password between 3-20 characters."
        # redirect to homepage, and include error as a query parameter in the URL
        return render_template('sign-up-home.html', password_error = error )

    if " " in password:
        error = "Passwords cannot contain spaces. Please try again."
        return render_template('sign-up-home.html', password_error = error )

    if not(verify_password == password):
        error ="Does not match the password entered. Please try again"
        return render_template('sign-up-home.html', verify_password_error = error )

    if not(email):
        pass
    elif email:
        for char in email:
            total_at = 0
            if char == "@":
                total_at += 1

            if not(total_at == 1):
                error = "Not a valid email. Please try again."
                return render_template('sign-up-home.html', email_error = error, email = email)
            else:
                pass
        for char in email:
            total_period = 0
            if char == ".":
                total_period += 1
        
            if not(total_period == 1):
                error = "Not a valid email. Please try again."
                return render_template('sign-up-home.html', email_error = error, email = email )
            else:
                pass
        if len(email) < 3 or len(email) > 20:
            error = "Not a valid email. Please try again."
            return render_template('sign-up-home.html', email_error = error, email = email )
        if " " in email:
            error = "Not a valid email. Please try again."
            return render_template('sign-up-home.html', email_error = error, email = email )
    return render_template("welcome.html", username=user_name)

@app.route("/welcome")
def welcome():
    user_name = request.form['username']
    return render_template("welcome.html", username=user_name)

@app.route("/")
def index():
    return render_template('sign-up-home.html')
app.run()
