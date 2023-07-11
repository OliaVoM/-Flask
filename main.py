from flask import Flask, url_for, request  # url_for сама пропишет путь к файлу, связывает каталог статического каталога с изображение

app = Flask(__name__)  # присваиваем имя нашему приложению


@app.route('/')  # делаем декоратор для главной страницы, говорит о том, на какую страницу пойдем
@app.route('/index')  #
def index():  # ф-ция кот. будет что-то делать когда перейдем на главную страницу
    return 'Адмирал!<br><a href="/slogan">Слоган</a>'

@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<h1>Постер к фильму</h1>
<img src="{url_for('static', filename='images/admiral1.png')}" 
alt="Здесь должна была быть картинка, но не нашлась">
<p class="grey">И крепка, как смерть, любовь!</p>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</body>
</html>"""

@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь!<br><a href="/">Назад</a>'

@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]  # лист заполнить от 10 до 0 с шагом 1
    lst.append('Start!!!')  # как только ноль надо вернуть Cтарт
    return '<br>'.join(lst)  # все они будут на писаны

@app.route('/greeting/<username>')
def greeting(username):
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{username}</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    <h1>Привет, {username}</h1>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
    </body>
    </html>"""
@app.route('/slideshow')
def slideshow():
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Постер</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/sea_1.jpg')}" class="d-block w-100" alt="Фото">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/sea_2.jpg')}" class="d-block w-100" alt="Фото">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/sea_3.jpg')}" class="d-block w-100" alt="Фото">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-target="#carouselExampleControls" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-target="#carouselExampleControls" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </button>
</div>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
    </body>
    </html>"""

@app.route('/nekrasov')
def nekrasov():
    return f"""<!DOCTYPE html>
    <html lang="en">
    <div class="container">
    <!-- Content here -->
    </div>
    
    <head>
        <meta charset="UTF-8">
        <title class="grey">Николай Алексеевич Некрасов</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    <h1>Николай Алексеевич Некрасов "Родина"</h1>
    <img src="{url_for('static', filename='images/nekrasov.png')}" 
    alt="Здесь должна была быть картинка, но не нашлась">
    <div class="bg-success text-warning">
    И вот они опять, знакомые места,</div>
    <div class="bg-info text-warning">
    Где жизнь текла отцов моих, бесплодна и пуста,</div>
    <div class="bg-secondary text-warning">
    Текла среди пиров, бессмысленного чванства,</div>
    <div class=".bg-primary text-warning">
    Разврата грязного и мелкого тиранства;</div>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
    </body>
    </html>"""

@app.route('/variants/<int:var>')
def variants(var):
    if var == 1:
        return f"""<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <title>Варианты выбора</title>
                </head>
            <body>
                <dl>
                    <dt>Пан или пропал</dt>
                    <dd>А что, нельзя выжить, став паном?</dd>
                </dl>
            </body>
            </html>"""
    elif var == 2:
        return f"""<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">                    
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <title>Варианты выбора</title>
                </head>
                <body>
                    <dl>
                        <dt>Даже если Вас съели, у Вас есть два</dt>
                        <dd>А в рассказах Мюнхаузена есть другой способ.</dd>
                    </dl>
                </body>
                </html>"""
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



if __name__ == '__main__':  # любой скрипт,  кот. будем запускать он будет иметь имя main
    app.run(host='127.0.0.1', port=5000, debug=True)  # указываем по какому хосту будем тестить наш сайт = по локальному,
                                # также надо указать порт (16 разрядов выделено под порты) можно добавить debug on/off включаем ли отладку
