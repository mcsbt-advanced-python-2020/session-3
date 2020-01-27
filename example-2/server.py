# -*- coding: utf-8 -*-
#%%
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def render_html():
    return send_from_directory("example-2/html", "index.html")

app.run()