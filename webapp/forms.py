from flask_wtf import FlaskForm
from wtforms import (StringField, FloatField)
from wtforms.validators import InputRequired, Length, NumberRange

class GradeForm(FlaskForm):
    class_name = StringField("Class Name", validators=[InputRequired(),
                                                        Length(min=2, max=50)])
    current_grade = FloatField("Current Grade", validators=[InputRequired(), NumberRange(min = 0, max = 100)])
    final_weight = FloatField("Weight of Final", validators=[InputRequired(), NumberRange(min = 0, max = 100)])
    desired_grade = FloatField("Desired Grade", validators=[InputRequired(), NumberRange(min = 0, max = 100)])