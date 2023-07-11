from flask import Flask, url_for, request, redirect
from flask import render_template

app = Flask(__name__)  # присваиваем имя нашему приложению


@app.route('/')
@app.route('/index')
def index():
    return redirect('form_sample') # ,eptckjdyst htlbhtrn

@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь!<br><a href="/">Назад</a>'


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
        with open('./templates/user_form.html', 'r', encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        print(request.method)
        print(request.form['fname'])
        print(request.form['sname'])
        return 'Форма отправлена'


if __name__ == '__main__':  # любой скрипт,  кот. будем запускать он будет иметь имя main
    app.run(host='127.0.0.1', port=8000, debug=True)  # указываем по какому хосту будем тестить наш сайт = по локальному,
    # также надо указать порт (16 разрядов выделено под порты) можно добавить debug on/off включаем ли отладку
