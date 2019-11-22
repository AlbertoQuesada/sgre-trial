# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:40:57 2019

@author: alberto.quesada
"""

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"), debug=True) 