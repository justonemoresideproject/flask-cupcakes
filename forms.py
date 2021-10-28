from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class CupcakeForm(FlaskForm):
    """Form for cupcakes"""

    flavor = StringField('Cupcake Flavor', validators=[InputRequired()])
    size = StringField('Cupcake Size')
    rating = StringField('Cupcake Rating')
    image = StringField('Image URL')