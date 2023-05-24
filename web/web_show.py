# from flask import Flask, request,  redirect, render_template,session

from flask import Flask, render_template, url_for

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/3')
def about():
    return render_template('index.3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1111, debug=False)

