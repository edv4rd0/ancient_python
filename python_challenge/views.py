from flask import Flask, session, url_for, request, flash
from flask import render_template, redirect

from python_challenge import app, mongo
from python_challenge import permissions
from python_challenge.forms import LoginForm



@app.route("/")
def index():
    """Main index of application."""
    return render_template("index.html")

    
@app.route("/add_record/")
@permissions.requires('add_record')
def add_record():
    """Add a record to the whatsit"""
    return "Record added"


@app.route("/edit_record/")
@permissions.requires('edit_record')
def edit_record():
    """Edit a record"""
    return "Edit Record"
    
    
@app.route("/remove_record/")
@permissions.requires('remove_record')
def remove_record():
    """Remove a record"""
    return "Remove Record"


@app.route("/generate_report/")
@permissions.requires('generate_report')
def generate_report():
    """Generate a report"""
    return "Generate Report"


@app.route("/login/", methods=["GET", "POST"])
def login():
    """Login to the site using the permissions method to validate"""
    form = LoginForm()
    if request.method == 'POST':
        if permissions.authenticate(request.form['username'], 
            request.form['password']):
            session['username'] = request.form['username']
            session['logged_in'] = True
            flash("Logged in successfully.")
            return redirect(url_for("index"))
    return render_template("login.html", form=form)


@app.route('/logout/')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run()
