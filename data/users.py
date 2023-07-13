import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash  # цепная работа по обеспечению безопасности
from werkzeug.security import check_password_hash

class User(SqlAlchemyBase):  # какие будут поля в таблице
    __tablename__ = 'users'  # служебный атрибут, кот. укажет нашей таблице, что файл будет создан с таким-то именем

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)   # sqlAlchemyBase будет строкой, т.к. это имя
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # нельзя хранить пароль в открытом виде, поэтому хэшируем, но в другом месте
    create_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    news = orm.relationship('News', back_populates='user')  # обращаться надо к классу News, мы работаем не на уровне таблиц, а класса
    # # back_populates указывает не на таблицу, а на атрибут класса News

    def __repr__(self):
        return f'{self.name} - {self.email}'

    def set_password(self, password):  # вводим пароль
        self.hashed_password - generate_password_hash(password)  # преобразовывает пароль в свой код

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)  # здесь сверяет пароль в зашифрованном виде
                    # с паролем введенном и сохраненном в БД, возвращает True - если верно




