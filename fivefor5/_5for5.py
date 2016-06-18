from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from forms import SongForm

#from logging import DEBUG

app = Flask(__name__)
#app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\xddg\xf8\xab\xe9\x94\x97\x05rD\x0f\xb8\xaa\x17\xd4\x82\x1cY\xc8wHl6\x1e'

class User:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def initials(self):
		return "{}. {}.".format(self.firstname[0], self.lastname[0])



@app.route('/')
@app.route('/index')
def index():
#	return render_template('index.html', title="Title passed from view to template", 
#								text="Text passed from view to template ")
	return render_template('index.html')

songlist = ["Mexican Cousin", "The Curtain With", "Sample in a Jar", "Yarmouth Road", "The Landlady", "Army of One", "Kill Devil Falls", "Bathtub Gin", "Funky Bitch", "The Moma Dance", "Saw It Again", "Down with Disease", "Roggae", "Crosseyed and Painless", "Farmhouse", "Mike's Song", "Bug", "Weekapaug Groove"]



@app.route('/api/v1.0/songs', methods=['GET', 'POST'])
def get_songs():
	return jsonify(results=songlist)




@app.route('/add', methods=['GET', 'POST'])
def add():
	form = SongForm()
	if form.validate_on_submit():
		song = form.song.data
		store_song(song)
		flash("Stored Song'[]'".format(description))
		return redirect(url_for('index'))
	return render_template('add.html', form=form)



'''	
if request.method == "POST":
		url = request.form['url']
		store_bookmark(url)
		flash("Stored Bookmark '{}'".format(url))
		#app.logger.debug('stored url: ' + url)
		#flash("hello!")
		return redirect(url_for('index'))
	return render_template('add.html')
'''
def new_songs(num):
	return sorted(songlist)[:num]


@app.route('/signup')
def signup():
	return render_template('add.html')	

@app.route('/signin')
def signin():
	return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

#	app.run(host='0.0.0.0')
