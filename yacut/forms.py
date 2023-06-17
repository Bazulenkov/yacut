from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class UrlMapForm(FlaskForm):
    original_link = URLField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="required field"),
            URL(message="You input not a link"),
            Length(1, 256),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[Regexp(r"[a-zA-Z0-9]+"), Length(1, 16), Optional()],
    )
    submit = SubmitField("Создать")
