from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import create_engine

Base = declarative_base()



class Messages(Base, SerializerMixin):
    __tablename__ = 'messege'
    id = Column(Integer, primary_key=True)
    messages = Column(String)
    Date_Time = Column(String)
    username = Column(String(250))
    user_id = Column(Integer)
    emotion = Column(Integer)


engine = create_engine('sqlite:///base_of_users.db')
Base.metadata.create_all(engine)