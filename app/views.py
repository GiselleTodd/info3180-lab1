from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import ProfileForm
#from app.models import UserProfile
#from werkzeug.security import check_password_hash


'''

# Routing for your application.
# Put your routes below this comment
'''
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()

    #if form.validate_on_submit():
    return render_template('profile.html', form=form)

"""@app.route("/profiles/<userid>")
def profiles(userid):
    return render_template(url_for('profiles'))"""


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
