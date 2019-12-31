from htdoc import app
from flask import render_template, url_for, redirect

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash(f"Already logged in.")
        return redirect(url_for("dashboard.html"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if not is_safe_url(next_page):
                return flask.abort(400)
            flash(f"Logged in.")
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash(f"Failed to log in. Check username / password.")
            return redirect(url_for('login'))
    return render_template("login.html", title="Login", form=form)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash(f"Logged out.")
        return redirect(url_for("home"))
    else:
        flask.abort(403)

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
