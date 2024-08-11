from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from inventory_control.models import Location

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Location')

class AddInventoryForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    location_id = SelectField('Location', coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Add Inventory')

    def __init__(self, *args, **kwargs):
        super(AddInventoryForm, self).__init__(*args, **kwargs)
        self.location_id.choices = [(location.id, location.name) for location in Location.query.all()]

class RemoveInventoryForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    location_id = SelectField('Location', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Remove Inventory')

    def __init__(self, *args, **kwargs):
        super(RemoveInventoryForm, self).__init__(*args, **kwargs)
        self.location_id.choices = [(location.id, location.name) for location in Location.query.all()]