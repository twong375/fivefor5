#from wtforms import Form
from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, url

class SongForm(Form):
	song = StringField('song', validators=[DataRequired()])
	description = StringField('description')