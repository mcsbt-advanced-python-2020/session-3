# -*- coding: utf-8 -*-
#%%
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/images/show_image")
def send_image():
    return send_from_directory("example-1/img", "flask-logo.png")

app.run()