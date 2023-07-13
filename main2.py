from flask import Flask, url_for, request, redirect, make_response
from flask import render_template
import json, requests
from loginform import LoginForm
from data import db_session
from data.users import User
from data.news import News
from forms.user import RegisterForm
from data import db_sessionMR

app = Flask(__name__)  # присваиваем имя нашему приложению
# ошибка 404
app.config['SECRET_KEY'] = 'to short key'  # здесь пишется очень сложный ключ, для защиты от хакерских проделок
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/news.sqlite' # URI

@app.errorhandler(404) # если страница не существует будет отправлять на созданную стр well
def http_404_error(error):
    return redirect('/error404')

@app.route('/error404')
def well(): #  колодец
    return render_template('well.html')

@app.route('/')
@app.route('/index1')
def index1():
    # return render_template('index1.html', title='Работа с шаблонами', username="Слушатель")  # после этого в шаблон index.html вставится нужный
    # param = {}
    # param['username'] = "Слушатель"
    # param['title'] = "Расширяем шаблоны"
    # return render_template('index1.html', **param)
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template('index1.html', title='Новости', news=news)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)

@app.route('/news')
def news():
    with open('news.json', "rt", encoding='utf-8') as f:  # открываем файл и считываем строки
        news_list = json.loads(f.read())  # загрузим ту строку, кот. прочитал, строку передадим методу loads
    return render_template('news.html', title="Новости", news=news_list)
    # lst = ['ANN', 'Tom', 'Bob']
    # return render_template('news.html', title="FOR", news=lst)

@app.route('/vartest')
def vartest():
    return render_template('var_test.html', title="Переменные в HTML")

@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь!<br><a href="/">Назад</a>'

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():  # если форма заполнена, надо проверить поля на совпадение пароля и повтроного пароля+
        if form.password.data != form.password_again.data:  # сравниваем данные
            return render_template('register.html', title='Проблемы с регистрацией', message='Пароли не совпадают', form=form)
        db_sess = db_session.create_session()  # подцепляемся к БД, если if отработал
        if db_sess.query(User).filter(User.email == form.email.data).first(): # если такой пароль есть в БД, то отработает условие, что емейл такой уже есть, а нам не надо
            return render_template('register.html', title='Проблемы с регистрацией', message='Такой пользователь уже есть', form=form)
        user = User(name=form.name.data, email=form.email.data, about=form.about.data)
        user.set_password(form.password.data)  # присваиваем пароль, проверка была в первом if
        db_sess.add(user)  # добавляем в БД
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)  # раз форму вызвали form = LoginForm() , значить
                                                                # форму туда и должны передать -> вводим ещё один параметр form
                                                                # создаем файл login.html


@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'GET':
        return render_template('weather_form.html', title='Введите город')
    elif request.method == 'POST':
        town = request.form.get('town')
        data = {}
        key = 'fdaa3fcaf6fabd1b949b0025881f9855'
        url = 'https://api.openweathermap.org/data/2.5/weather/'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        code = weather['cod']  # надо получить код, 200 - нашли город
        icon = weather['weather'][0]['icon']  # чтобы вытащить иконку из полученного списка на странице в примере
                                        # берем ссылку в которой для примера стоит ссылка на иконку 10d(код иконки на сайте),
                                        # чтобы получить иконку текущего запроса,вместо 10 вставить значение
                                        # icon код jinja weather.html
        # temp = weather['main']['temp']
        # wind = weather['wind']['deg']
        # speed = weather['wind']['speed']
        temperature = weather['main']['temp']
        data['code'] = code
        data['icon'] = icon
        data['temp'] = round(temperature, 1)
        return render_template('weather.html', title=f'Погода в городе{town}', town=town, data=data)


@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]  # лист заполнить от 10 до 0 с шагом 1
    lst.append('Start!!!')  # как только ноль надо вернуть Cтарт
    return '<br>'.join(lst)  # все они будут на писаны

@app.route('/load_photo', methods=['GET', 'POST']) # если у формы будет метод GET, то все появится на странице
def load_photo():
    if request.method == 'GET':
        return f"""
        <form class="login_form" method="post" enctype="multipart/form-data>
            <div class="form-group">    
                <label for="photo">Приложите фото:</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <br>
        <button type="submit" class="btn btn-primary">Отправить</button>            
        </form>
        """
    elif request.method == 'POST':
        f = request.files['file']  # сюда прочитали файл
        f.save('./static/images/loaded.png')  # куда сохраняем, переименовываем принудительно
        return '<h1>Файл у Вас на сервере </h1>'

#@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count:
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count',
                       str(visit_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response('Вы впервые здесь за 2 года')
        res.set_cookie('visit_count', '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res

@app.route('/form_sample', methods=['GET', 'POST'])  # methods=['GET', 'POST'] Разрешили оба метода
def form_sample():
    if request.method == 'GET':
        return render_template('user_form.html', title='Форма')
    elif request.method == 'POST':
        f = request.files['file']  # сюда прочитали файл
        f.save('./static/images/loaded.png')  # куда сохраняем, переименовываем принудительно
        myform = request.form.to_dict()  # получаем форму и превращаем её в словарь
        return render_template('filled_form.html', title='Ваши данные', data=myform)


if __name__ == '__main__':  # любой скрипт, кот. будем запускать он будет иметь имя main
    db_session.global_init('db/news.sqlite')  # в db должна появиться БД
    app.run(host='127.0.0.1', port=8000, debug=True)  # указываем по какому хосту будем тестить наш сайт = по локальному,
    # # также надо указать порт (16 разрядов выделено под порты) можно добавить debug on/off включаем ли отладку
    # user = User()
    # user.name = 'Voldemar'
    # user.about = '53 years old'
    # user.email = 'voldemar@mail.ru'
    # db_sess = db_session.create_session()
    # db_sess.add(user)

    # #
    # user = User()
    # user.name = 'Dmitry'
    # user.about = 'gamer'
    # user.email = 'ljedmitriy@mail.ru'
    # db_sess = db_session.create_session()
    # db_sess.add(user)


    # user = User()
    # user.name = 'Mark'
    # user.about = 'plumer'
    # user.email = 'ljeplumer@mail.ru'
    # db_sess = db_session.create_session()  #отвечает за подключение к нашей БД
    # db_sess.add(user)

    # db_sess = db_session.create_session()  # отвечает за подключение к нашей БД
    # id = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title='Новости от Владимира', content='Пришел домой', user_id=id.id, is_private=False)  # добавляем новость
    # db_sess.add(news)

    # db_sess = db_session.create_session()  # отвечает за подключение к нашей БД
    # user = db_sess.query(User).filter(User.id == 1).first() # получили юзера с номером 1
    # subj = News(title='Новости от Владимира №3', content='Поехал в поликлинику', user_id=user.id, is_private=False) # добавляем новость
    # user.news.append(subj)  # обращаемся напрямую через методы классов
    #
    # # db_sess = db_session.create_session()  # отвечает за подключение к нашей БД
    # user = db_sess.query(User).filter(User.id == 1).first() # получили юзера с номером 1
    # for news in user.news():
    #     print(news)


    # user = db_sess.query(User).first()  # получить первого пользователя из БД
    # users = db_sess .query(User).all()
    # for user in users:
    #     print(user)

    # users = db_sess.query(User)
    # for user in users:
    #     print(user)

    # users = db_sess.query(User).filter(User.email.notilike('%v%')) # вывести пользователя, у кот. нет буквы v,
    # for user in users:
    #     print(user)

    # users = db_sess.query(User).filter(User.id == 1).first()  # поменять ему имя на Vladimir
    # user.name = 'Vladimir'

    # users = db_sess.query(User).filter(User.name == "Dmitry") # удалить пользователя
    # db_sess.delete(user)

    # db_sess.commit()






