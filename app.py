from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html', _anchor='about')

@app.route('/projects')
def projects():
    return render_template('index.html', _anchor='projects')

@app.route('/contact')
def contact():
    return render_template('index.html', _anchor='contact')

if __name__ == '__main__':
    app.run(debug=True)