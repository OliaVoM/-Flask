import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase

__tablename__ = 'users'  # служебный атрибут, кот. укажет нашей таблице, что файл будет создан с таким-то именем
class User(SqlAlchemyBase):  # какие будут поля в таблице
    id = sqlalchemy.column(sqlalchemy.Integer, primary_key=True, autoincriment=True)   # sqlAlchemyBase будет строкой, т.к. это имя
    name = sqlalchemy.column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.column(sqlalchemy.Integer, nullable=True)
    email = sqlalchemy.column(sqlalchemy.Integer, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.column(sqlalchemy.String, nullable=True)  # нельзя хранить пароль в открытом виде, поэтому хэшируем, но в другом месте
    create_date = sqlalchemy.column(sqlalchemy.DateTime, default=datetime.datetime.now())

