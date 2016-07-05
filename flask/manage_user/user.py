import os
import MySQLdb as my
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    db = my.connect("localhost","root","password","test")
    cursor = db.cursor(my.cursors.DictCursor) 
    return cursor

@app.route("/")
def show_user():
    cursor = connect_db()
    cursor.execute("select user_name, password, email, first_name, last_name from user order by user_id desc")
    user=cursor.fetchall()
    print user
    return render_template("show_user.html", users=user)


