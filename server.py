from flask import Flask, render_template, redirect, request
from forms import SignUpForm
from pony import orm
from database import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sofia-best-girl'


words = [
	{
		"english": "woman",
		"nahuatl": "cihuatl"
	},
	{
		"english": "corn",
		"nahuatl": "centli"
	}
]
@app.route('/newLesson')
def newLesson():
    return render_template('newLesson.html')


@app.route('/newWord', methods=['GET', 'POST'])
def newWord():
	word_english = request.form['word_english']
	word_nahuatl = request.form['word_nahuatl']

	new_word = {
		"english": word_english,
		"nahuatl": word_nahuatl
	}
	words.append(new_word)
	return render_template('newLesson.html')


@app.route('/nahuatlLesson')
def nahuatlLesson():
    return render_template('nahuatlLesson.html', words = words)
@app.route('/')
def home():
    return render_template('browse.html')


@app.route('/about')
def about():
    return "About page"


@app.route('/blogtrue')
def blogtrue():
    return render_template('blogtrue.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/nahuatl')
def nahuatl():
    return render_template('nahuatl.html')

@app.route('/maya')
def maya():
    return render_template('maya.html')


@app.route('/signup', methods=['GET', 'POST'])
@orm.db_session
def signup():
    form = SignUpForm()
    if form.is_submitted():
        return render_template('home_page.html', form=form)

    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run()
