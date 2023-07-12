from flask import Flask, url_for, request, redirect
from flask import render_template
import json, requests
from loginform import LoginForm
from data import db_session

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
    # return render_template('index.html', title='Работа с шаблонами', username="Слушатель")  # после этого в шаблон index.html вставится нужный
    param = {}
    param['username'] = "Слушатель"
    param['title'] = "Расширяем шаблоны"
    return render_template('index1.html', **param)

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

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form) # раз форму вызвали form = LoginForm() , значить
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


@app.route('/form_sample', methods=['GET', 'POST'])  # methods=['GET', 'POST'] Разрешили оба метода
def form_sample():
    if request.method == 'GET':
        return render_template('user_form.html', title='Форма')
    elif request.method == 'POST':
        f = request.files['file']  # сюда прочитали файл
        f.save('./static/images/loaded.png')  # куда сохраняем, переименовываем принудительно
        myform = request.form.to_dict()  # получаем форму и превращаем её в словарь
        return render_template('filled_form.html', title='Ваши данные', data=myform)


if __name__ == '__main__':  # любой скрипт,  кот. будем запускать он будет иметь имя main
    db_session.global_init('db/news.sqlite')  # в db должна появиться БД
    app.run(host='127.0.0.1', port=8000, debug=True)  # указываем по какому хосту будем тестить наш сайт = по локальному,
    # также надо указать порт (16 разрядов выделено под порты) можно добавить debug on/off включаем ли отладку
