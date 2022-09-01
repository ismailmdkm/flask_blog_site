from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = 'e49e40b1ecb9bddf401db4ca38197c62'

posts = [
    {
        'author': 'Mohamed Ismail',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2022'
    },
    {
        'author': 'Ibrahim',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"You have logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash(f"Unsuccessful login!", 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
