from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.fields.html5 import DecimalRangeField

class ParameterForm(FlaskForm):
	prefix = StringField('Prefix')
	temperature = DecimalRangeField('Temperature', 
		default=1.0)
	submit = SubmitField('Make village names')
	extra_options = BooleanField(False)