from flask import Flask, render_template, redirect, request
from forms import SignUpForm
from pony import orm
from database import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sofia-best-girl'


@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/nahuatl')
def nahuatl():
    return render_template('nahuatl.html')


@app.route('/signup', methods=['GET', 'POST'])
@orm.db_session
def signup():
    form = SignUpForm()
    if form.is_submitted():
        return render_template('home_page.html', form=form)

    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run()
