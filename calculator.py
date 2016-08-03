import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
	 
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("home.html")
	
@app.route('/calculate',methods = ['GET','POST'])
def calculate():
	result =  int(request.form['title']) + int(request.form['text'])
	return render_template("resultpage.html", result=result)
app.run()