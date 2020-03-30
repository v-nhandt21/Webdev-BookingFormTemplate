
from flask import Flask, request, jsonify, render_template,json, abort,flash, redirect
app = Flask(__name__, static_url_path='/static')



@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template('AutoFillAddress.html')

@app.route("/test1", methods=['GET', 'POST'])
def test1():
    return render_template('t.html')

if __name__ == "__main__":
    app.run(port=5018)
