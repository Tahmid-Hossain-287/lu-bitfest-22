from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/<path:page_name>')
def hello(page_name="index.html"):
    return render_template({page_name})

