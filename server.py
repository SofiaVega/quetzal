from flask import Flask, render_template, redirect, request
from forms import SignUpForm
from pony import orm
from database import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sofia-best-girl'


@app.route('/')
def home():
    return "Sofia is amazing <3"


@app.route('/about')
def about():
    return "About page"


@app.route('/blog')
def blog():
    return "This is a blog"

@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/signup', methods=['GET', 'POST'])
@orm.db_session
def signup():
    form = SignUpForm()
    if form.is_submitted():
        User(username=form.username.data, password=form.password.data)
        users = orm.select(u for u in User)
        return render_template('user.html', result=users)

    return render_template('signup.html', form=form)


@app.route('/users')
@orm.db_session
def list_users():
    users = orm.select(u for u in User)
    return render_template('user.html', result=users)


@app.route('/blog/<string:blog_id>')
def view_blog(blog_id):
    posts = [
        {"author": "Sofia", "title": "I love Bython"},
        {"author": "Eduardo", "title": "I like C#"}
    ]

    return render_template("blog.html", author={"name": "Sofia", "age": 21, "mayuino_here": True}, posts=posts)


if __name__ == '__main__':
    app.run()
