from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html')
