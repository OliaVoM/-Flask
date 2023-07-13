from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, TextAreaField
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired

# сначала создадим класс и унаследуем его от нашего FlaskForm
class RegisterForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired()])  # в forms validators cсуществуют все формы, после того как
    # человек отпарвил адрес и почту, он является неподтвержденным пользователем, приходит писмьмо для подтверждения, программа
    # генерирует строку-ссылку, при нажатии на неё произойдет сличение с БД и происходит регистрация
    password =PasswordField('Пароль', validators=[DataRequired()]) # ('Пароль', validators=[DataRequired()]), 'Пароль' - это label в файле regiter.html
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Ваше имя', validators=[DataRequired()])  # validators=[DataRequired()] надо писатьвезде, защитит от незаполненных полей - будет ругаться
    about = TextAreaField('Немного о себе')
    submit = SubmitField('Войти')

