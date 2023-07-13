import sqlalchemy as sa
import sqlalchemy.orm as orm  # будем обращаться к элементам БД как будто к атрибутам данного класса
from sqlalchemy.orm import Session  # будет отвечать за каждую сессию работы в БД

SqlAlchemyBase = orm.declarative_base()  # переменная, объект с пом. кот мы все будем делать

created = None  # глобальная переменная, кот. будет отвечать создана ли сессия


def global_init(db_file): # пора запускать БД, глобальная инициализация БД (db_file) - что подадим, файл с таким именем и будет создал, внутри ф-ции мы не можем опрерировать с голб. переменнами, если сами этого не разрешим
    global created  #  внутри ф-ции мы не можем опрерировать с голб. переменнами, если сами этого не разрешим

    if created:
        return  # если БД уже была создана, то выходим из if

    if not db_file or not db_file.strip():  # если не была создана ранее, и по каким-то причинам там есть проблемы, забыли подключить, то будет выведено исключение
        raise Exception("Забыли подключить файл базы!")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'  # (connection string) подключаем бызу и проверяем не используем ли тот же поток данных
     # для отладки, потом можно отключить
    print(f'Вы подключились к базе данных {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)  # подключаем движок для создания БД, для этого понадобиться import sqlalchemy as sa, не надо рассказывать, что движок как и где подключен
    created = orm.sessionmaker(bind=engine)  # связываем глобальную переменную с созданным движком


    from . import all_models    # точка означает, что подключаемся по той же директории

    SqlAlchemyBase.metadata.create_all(engine)
     # анататор функции -> будет возвращать сессию, не зависимо будет этот знак или нет

def create_session() -> Session:
    global created
    return created()
