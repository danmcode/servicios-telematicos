#app/views.py

from flask import render_template

from app import app
from app import data as inf

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
        return render_template("about.html")

@app.route('/articles')
def articles ():
        return render_template("articles.html", articles = inf.Articles())

@app.route('/articles_details/<int:id>')
def articles_details (id):
        try:
                id=int(id)
                bo = inf.Articles()[id-1]["body"]
                ti = inf.Articles()[id-1]["title"]
                aut = inf.Articles()[id-1]["author"]
                cre = inf.Articles()[id-1]["create_date"]
        except:
                abort(404)
        return render_template("details.html", numId = id, body = bo, author=aut, create_date = cre, title = ti)