from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return redirect(f'https://github.com/search?q={query}')

@app.route('/repos/pryzma')
def pryzma_repo():
    return render_template('repos/pryzma/pryzma.html')

@app.route('/repos/pryzma-programming-language')
def pryzma_programming_language_repo():
    return render_template('repos/pryzma-programming-language/pryzma-programming-language.html')

if __name__ == '__main__':
    app.run(debug=True)