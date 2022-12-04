from flask import render_template, url_for
# url_for is to to avoid handling of URLs manually (e.g. if we change a root URL we would need to change all templates/web page this URL is present).
# Look at layout page for usage
from blog import app

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About Me')