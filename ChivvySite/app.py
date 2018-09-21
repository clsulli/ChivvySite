from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def dash():
    return render_template('base_dash.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username='clsulli', plan_level='Basic Plan')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
