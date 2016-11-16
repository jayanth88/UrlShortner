from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request

from controller.urlProcessor import UrlProcessor


app = Flask(__name__)
processor= UrlProcessor()

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_url_request():
    print str('VALUE :'+ request.form['urlName'])
    url_id = processor.processUrl(request.form['urlName'])
    return str(url_id)


if __name__ == '__main__':
    app.run()
