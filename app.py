from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/repos/pryzma')
def pryzma_repo():
    return render_template('repos/pryzma/pryzma.html')


if __name__ == '__main__':
    app.run(debug=True)