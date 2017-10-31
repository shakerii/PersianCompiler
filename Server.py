from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def static_page():
    return render_template('index.html')


@app.route('/compiler', methods=['POST'])
def compiler():
    print(request.form['name'])
    print(request.form['code'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
