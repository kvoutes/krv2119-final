##########################
# Name: Kamryn Voutes
# UNI: krv2119
# Description: webpage with personal bio, class description, and Kate Mckinnon pages
##########################
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def bio():
    return render_template("index.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/Kate")
def Kate():
    return render_template("Kate.html")
#start the server
if __name__ == "__main__":
    app.run()