from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy?charset=utf8')
BaseModel = declarative_base()


class Girl(BaseModel):
    __tablename__ = 'girl'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    gtb = relationship('Boy', backref='btg', secondary='hotel')


class Boy(BaseModel):
    __tablename__ = 'boy'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)


class Hotel(BaseModel):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True)
    bid = Column(Integer, ForeignKey('boy.id'))
    gid = Column(Integer, ForeignKey('girl.id'))


BaseModel.metadata.create_all(engine)
