import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase

__tablename__ = 'users'  # служебный атрибут, кот. укажет нашей таблице, что файл будет создан с таким-то именем
class User(SqlAlchemyBase):  # какие будут поля в таблице
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincriment=True)   # sqlAlchemyBase будет строкой, т.к. это имя
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.Integer, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # нельзя хранить пароль в открытом виде, поэтому хэшируем, но в другом месте
    create_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())

