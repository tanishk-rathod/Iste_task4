from flask import Flask,render_template,request,session,redirect,flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL
from datetime import datetime
import os,json,math




app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.1/ISTE2"
app.secret_key = 'secret key'

# db=SQLAlchemy(app)
# db=SQLAlchemy()

# from models import Contact, Register
# from forms import RegistrationForm, ContactForm

@app.route("/")
def home():
    return render_template("index.html", page=1)

# @app.route("/contact", methods=['GET','POST'])
# def contact():
#     form = ContactForm()
#     if request.method == 'POST':
#         entry = Contact(Name=form.name.data,Email=form.email.data,Subject=form.subject.data,Message=form.message.data)
#         db.session.add(entry)
#         db.session.commit()
#         return redirect('/') 
#     return render_template('contact.html',page=4, form=form)

# @app.route("/register", methods=['GET','POST'])
# def register():
#     form = RegistrationForm()
#     if request.method == 'POST':
#         entry = Contact(Name=form.name.data,Email=form.email.data,Subject=form.subject.data,Message=form.message.data)
#         db.session.add(entry)
#         db.session.commit()
#         return redirect('/') 
#     return render_template('register.html', form=form)


# @app.route("/about")
# def about():
#     return render_template('about.html', page=2)

# @app.route("/speakers")
# def speakers():
#     return render_template('speakers.html', page = 3)

# @app.route("/aboutted")
# def aboutted():
#     return render_template('aboutted.html')




app.run(debug=True, port=8000)

