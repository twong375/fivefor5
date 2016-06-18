from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify, abort
from flask.ext.sqlalchemy import SQLAlchemy
from firebase import firebase
from forms import SongForm
import psycopg2
from flask_cors import CORS
from celery import Celery

#from logging import DEBUG

app = Flask(__name__)
CORS(app)
#app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\xddg\xf8\xab\xe9\x94\x97\x05rD\x0f\xb8\xaa\x17\xd4\x82\x1cY\xc8wHl6\x1e'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

'''
class song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(64), index=True)
    song_display_name = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Song %r>' % (self.song_name)
'''
class User:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def initials(self):
		return "{}. {}.".format(self.firstname[0], self.lastname[0])


def store_song(song):
	songlist.append(song)


@app.route('/')
@app.route('/index')
def index():
#	return render_template('index.html', title="Title passed from view to template", 
#								text="Text passed from view to template ")
	return render_template('index.html')

songlist = ["Mexican Cousin", "The Curtain With", "Sample in a Jar", "Yarmouth Road", "The Landlady", "Army of One", "Kill Devil Falls", "Bathtub Gin", "Funky Bitch", "The Moma Dance", "Saw It Again", "Down with Disease", "Roggae", "Crosseyed and Painless", "Farmhouse", "Mike's Song", "Bug", "Weekapaug Groove"]

songs = [
	{
		"id": 1,
		"name": "harpua",
		"datelastplayed": None
	},
	{
		"id": 2,
		"name": "Sand",
		"datelastplayed": None
	},
	{
		"id": 3,
		"name": "Tweezer",
		"datelastplayed": None
	},
	{
		"id": 4,
		"name": "Maze",
		"datelastplayed": None
	},
	{
		"id": 5,
		"name": "Drowned",
		"datelastplayed": None
	}
	]

@app.route('/api/v1.0/songs', methods=['GET'])
def get_songs():
	return jsonify({'songs': songs})


'''
@app.route('/json', methods=['GET'])
def get_songs_json():
    host = 'ec2-54-197-230-161.compute-1.amazonaws.com'
    dbname = 'd6l8miq2r8htqp'
    user = 'fexwmpttektrdn'
    password = 'NfW0iifDUW4n_kevHD_MfTJFTb'
    port = 5432
     
    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'"% (host, dbname, user, password, port)
    print "Connecting to database\n ->%s" % (conn_string)
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print "Connected!\n"
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

    #cursor.execute("SELECT * FROM dim_songs")
    cursor.execute("SELECT array_to_json(array_agg(view_song_list_cached)) FROM view_song_list_cached")
    return str(cursor.fetchall())
    #records = cursor.fetchall()
    #return str(records)
    #return render_template('jsondata.html', records=records)
'''

@app.route('/json', methods=['GET'])
def get_songs_json():
    host = 'ec2-54-197-230-161.compute-1.amazonaws.com'
    dbname = 'd6l8miq2r8htqp'
    user = 'fexwmpttektrdn'
    password = 'NfW0iifDUW4n_kevHD_MfTJFTb'
    port = 5432
     
    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'"% (host, dbname, user, password, port)
    print "Connecting to database\n ->%s" % (conn_string)
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print "Connected!\n"
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

    #cursor.execute("SELECT * FROM dim_songs")
    cursor.execute("SELECT array_to_json(array_agg(view_song_list_cached)) FROM view_song_list_cached")
    for row in cursor:
    	return jsonify(row)



    #return str(cursor.fetchall())
    #records = cursor.fetchall()
    #return str(records)
    #return render_template('jsondata.html', records=records)








@app.route('/api/v1.1/songs', methods=['GET'])
def get_songs_db():
    host = 'ec2-54-197-230-161.compute-1.amazonaws.com'
    dbname = 'd6l8miq2r8htqp'
    user = 'fexwmpttektrdn'
    password = 'NfW0iifDUW4n_kevHD_MfTJFTb'
    port = 5432
     
    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'"% (host, dbname, user, password, port)
    print "Connecting to database\n ->%s" % (conn_string)
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print "Connected!\n"
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

    #cursor.execute("SELECT * FROM dim_songs")
    cursor.execute("SELECT array_to_json(array_agg(view_song_list_cached)) FROM view_song_list_cached")
    records = cursor.fetchall()
    return jsonify({'songs':records})
    #print(records)
    #return records
'''
@app.route('/api/v1.0/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
	song = [song for song in songs if song['id'] == song_id]
	if len(song) == 0:
		abort(404)
	return jsonify({'song': song[0]})
'''	

@app.route('/api/v1.1/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
	host = 'ec2-54-197-230-161.compute-1.amazonaws.com'
	dbname = 'd6l8miq2r8htqp'
	user = 'fexwmpttektrdn'
	password = 'NfW0iifDUW4n_kevHD_MfTJFTb'
	port = 5432

	conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'"% (host, dbname, user, password, port)
	try:
		conn = psycopg2.connect(conn_string)
		cursor = conn.cursor()
	except:
		exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
		sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
		#cursor.execute("select * from view_song_list_cached where song_id='%s'" % song_id)
		cursor.execute("select * from view_song_list_cached where song_id='7'")
		records = cursor.fetchall()
		return jsonify({'songs':records})
		#return jsonify({'songs':records})
''

'''
	song = [song for song in songs if song['id'] == song_id]
	if len(song) == 0:
		abort(404)
	return jsonify({'song': song[0]})
'''






@app.route('/add', methods=['GET', 'POST'])
def add():
	form = SongForm()
	if form.validate_on_submit():
		song = form.song.data
		description = form.description.data
		store_song(song)
		flash("Stored Song'[]'")
		return redirect(url_for('index'))
	return render_template('add.html', form=form)

'''
@app.route('/add', methods=['GET', 'POST'])
def add():
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

@app.route('/tasks')



@celery.task
def my_background_task(arg1, arg2):
    # some long running task here
    return result


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500


if __name__ == "__main__":
	#port = int(os.environ.get("PORT", 5000))
	#app.run(host='0.0.0.0', port=port)
	app.run(debug=True)