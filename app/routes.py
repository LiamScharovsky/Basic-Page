from app import app
from flask import render_template

#MAIN APPLICATION ROUTES
@app.route("/")
def home():
    return render_template ('home.html')

@app.route("/about")
def about():
    return render_template ('about.html')

@app.route("/contact")
def contact():
    return render_template ('contact.html')
