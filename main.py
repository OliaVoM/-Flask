from flask import Flask, url_for  # url_for сама пропишет путь к файлу

app = Flask(__name__)  # присваиваем имя нашему приложению


@app.route('/')  # делаем декоратор для главной страницы
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



if __name__ == '__main__':  # любой скрипт,  кот. будем запускать он будет иметь имя main
    app.run(host='127.0.0.1', port=8000, debug=True)  # указываем по какому хосту будем тестить наш сайт = по локальному,
                                # также надо указать порт (16 разрядов выделено под порты) можно добавить debug on/off включаем ли отладку
