from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])  # создали класс в отедельном файле
    password = PasswordField('Пароль', validators=[DataRequired()])  # validators проверяет введены ли данные
    remember_me = BooleanField('Запомнить меня')
    file = FileField('Файл')
    submit = SubmitField('Войтм')
    # если из формы добавлен файл, то обращаться к нему при обработке формы следует так:
    # f.form.<название поле с файлом>.data
