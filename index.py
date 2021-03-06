from flask import Flask, render_template, request, redirect, session, flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[0-9]')
PASS_REGEX = re.compile(r'.*[A-Z].*[0-9]')

app = Flask(__name__)
app.secret_key = "Secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():

    email_val = request.form["email_key"]
    first_val = request.form["first_key"]
    last_val = request.form["last_key"]
    password_val = request.form["password_key"]
    confirm_val = request.form["confirm_key"]

    for i in request.form:
        if len(request.form[i]) < 1:
            flash(i + " field cannot be blank!", "error")

    if NAME_REGEX.search(first_val) or NAME_REGEX.search(last_val):
        flash("Your name cannot contain any numbers", 'error')
    if len(password_val) < 8 or len(confirm_val) < 8:
        flash("Password should be more than 8 characters long.", "error")
    if not EMAIL_REGEX.match(email_val):
        flash("Invalid Email Address!", "email")
    if not PASS_REGEX.match(password_val):
        print session
        flash("Password must have at least 1 uppercase letter and 1 numeric value.", 'email')
    if password_val != confirm_val:
        flash("Your passwords didn't match. Please try again.", "email")
    
    
    if '_flashes' in session: 
        return render_template("index.html")
    else:
        flash("Thanks for submitting your information.", "success")
        return redirect("/")

app.run(debug = True)