from flask import Flask, render_template,send_from_directory
import time
app = Flask(__name__)


@app.route('/')
def download_file():
    filename = time.strftime("D%Y_%m_%d", time.localtime()) + ".xls"
    return send_from_directory("C:/Users/19160830821/Desktop/", filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
