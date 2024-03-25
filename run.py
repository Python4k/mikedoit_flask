from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Главная')

@app.route('/html_page')
def html_page():
    return render_template('html_page.html', title='HTML')

@app.route('/css_page')
def css_page():
    return render_template('css_page.html', title='CSS')

@app.route('/js_page')
def js_page():
    return render_template('js_page.html', title='JAVASCRIPT')

@app.route('/python_page')
def python_page():
    return render_template('python_page.html', title='PYTHON')

@app.route('/flask_page')
def flask_page():
    return render_template('flask_page.html', title='FLASK')

@app.route('/django_page')
def django_page():
    return render_template('django_page.html', title='DJANGO')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
